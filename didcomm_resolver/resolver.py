"""Didcommm Universal DID Resolver."""

import json
import logging
import os
from pathlib import Path
from typing import Callable, List, NamedTuple, Set, cast

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.connections.models.conn_record import ConnRecord
from aries_cloudagent.core.profile import Profile, ProfileSession
from aries_cloudagent.messaging.responder import BaseResponder
from aries_cloudagent.resolver.base import (
    BaseDIDResolver,
    DIDMethodNotSupported,
    DIDNotFound,
    ResolverError,
    ResolverType,
)
from aries_cloudagent.storage.base import BaseStorage
from aries_cloudagent.storage.error import StorageNotFoundError
from aries_cloudagent.storage.record import StorageRecord
import yaml

from .acapy_tools.awaitable_handler import (
    WaitingForMessageFailed,
    send_and_wait_for_response,
)
from .protocol.v0_9 import ResolveDID, ResolveDIDResult

LOGGER = logging.getLogger(__name__)


class ResolverConnection(NamedTuple):
    """Resolver Connection"""

    connection_id: str
    methods: Set[str]

    @classmethod
    def from_metadata_record(cls, record: StorageRecord):
        """Create from storage record."""
        return cls(record.tags["connection_id"], json.loads(record.value)["methods"])

    @classmethod
    async def from_connection_id(cls, session: ProfileSession, connection_id: str):
        """Return a resolver connection from a connection id"""
        record = await ConnRecord.retrieve_by_id(session, connection_id)
        record = cast(ConnRecord, record)
        metadata = await record.metadata_get(session, DIDCommResolver.METADATA_KEY)
        if not metadata:
            raise StorageNotFoundError(
                f"Connection identified by {connection_id} is not a resolver connection"
            )
        return cls(record.connection_id, metadata["methods"])

    def serialize(self):
        """Return json ready serialized representation."""
        return {"connection_id": self.connection_id, "methods": list(self.methods)}


class DIDCommResolver(BaseDIDResolver):
    """Universal DID Resolver with DIDCOMM messages."""

    METADATA_KEY = "didcomm_resolver"
    METADATA_METHODS = "methods"

    def __init__(self):
        """Initialize DIDCommResolver."""
        super().__init__(ResolverType.NON_NATIVE)
        self._supported_methods: Set[str] = set()

    async def setup(self, context: InjectionContext):
        """Load resolver specific configuration."""
        config_file = os.environ.get(
            "DIDCOMM_RESOLVER_CONFIG", Path(__file__).parent / "default_config.yml"
        )
        try:
            with open(config_file) as input_yaml:
                configuration = yaml.load(input_yaml, Loader=yaml.SafeLoader)
        except FileNotFoundError as err:
            raise ResolverError(
                f"Failed to load configuration file for {self.__class__.__name__}"
            ) from err

        if not isinstance(configuration, dict):
            raise ResolverError("Configuration file is not properly loaded")
        self.configure(configuration)

    def configure(self, configuration: dict):
        """Configure this instance of the resolver from configuration dict."""
        try:
            self._supported_methods = configuration["methods"]
        except KeyError as err:
            raise ResolverError(
                f"Failed to configure {self.__class__.__name__}, "
                "missing attribute in configuration: {err}"
            ) from err

    @property
    def supported_methods(self) -> Set[str]:
        """Return supported methods.

        The DIDCommResolver defines a set of methods that it is willing to attempt
        to resolve. Resolver connections supported methods must be a subset of this
        list in order for the method to be resolved on a given connection.
        """
        return self._supported_methods

    @classmethod
    async def set_resolver_connection(
        cls,
        session: ProfileSession,
        connection_id: str,
        methods: Set[str],
    ) -> ResolverConnection:
        """Register connection as a resolver connection."""
        # retrieve connection record for metadata lookup, where methods are persisted
        conn_record = await ConnRecord.retrieve_by_id(session, connection_id)
        conn_record = cast(ConnRecord, conn_record)
        await conn_record.metadata_set(
            session, cls.METADATA_KEY, {cls.METADATA_METHODS: list(methods)}
        )
        return ResolverConnection(connection_id=connection_id, methods=methods)

    @classmethod
    async def unset_resolver_connection(
        cls,
        session: ProfileSession,
        connection_id: str,
    ) -> str:
        """Remove registered resolver connection."""
        conn_record = await ConnRecord.retrieve_by_id(session, connection_id)
        conn_record = cast(ConnRecord, conn_record)
        await conn_record.metadata_delete(session, cls.METADATA_KEY)
        return connection_id

    @classmethod
    async def resolver_connections(
        cls,
        session: ProfileSession,
        matching: Callable[[ResolverConnection], bool] = None,
    ) -> List[ResolverConnection]:
        """Return all resolver connections."""
        storage = session.inject(BaseStorage)

        records = await storage.find_all_records(
            ConnRecord.RECORD_TYPE_METADATA, {"key": cls.METADATA_KEY}
        )
        records = cast(List[StorageRecord], records)
        resolver_connections = [
            ResolverConnection(
                record.tags["connection_id"], json.loads(record.value)["methods"]
            )
            for record in records
        ]
        if matching:
            resolver_connections = list(filter(matching, resolver_connections))

        return resolver_connections

    async def _resolve(self, profile: Profile, did: str) -> dict:
        """Resolve DID through remote universal resolver."""
        method = did.split(":")[1]
        async with profile.session() as session:
            responder = session.inject(BaseResponder)
            if not responder:
                raise ValueError("No responder on profile!")

            resolver_connections = await self.resolver_connections(
                session, matching=lambda res_conn: method in res_conn.methods
            )
            if not resolver_connections:
                raise DIDMethodNotSupported(
                    f"No resolver connection supporting {method} was found"
                )

        # Construct Resolve DID message
        resolve_did_message = ResolveDID(did=did)

        not_found_conn_ids = []
        for res_conn in resolver_connections:
            LOGGER.debug(
                "Sending resolve request to %s: %s",
                res_conn.connection_id,
                resolve_did_message,
            )

            try:
                response: ResolveDIDResult = await send_and_wait_for_response(
                    message=resolve_did_message,
                    response_type=ResolveDIDResult,
                    responder=responder,
                    timeout=30,
                    connection_id=res_conn.connection_id,
                )
                result = response.did_document
                if not isinstance(result, dict):
                    result = json.loads(result)
                return result
            except DIDNotFound:
                LOGGER.exception(
                    "Connection %s could not find DID %s", res_conn.connection_id, did
                )
                not_found_conn_ids.append(res_conn.connection_id)
                continue
            except WaitingForMessageFailed:
                LOGGER.exception(
                    "Querying %s for DID %s timed out", res_conn.connection_id, did
                )
                not_found_conn_ids.append(res_conn.connection_id)
                continue

        raise DIDNotFound(
            "DID not found on any resolver connections({})".format(
                ", ".join(not_found_conn_ids)
            )
        )
