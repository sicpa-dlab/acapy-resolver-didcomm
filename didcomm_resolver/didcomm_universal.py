"""Didcommm Universal DID Resolver."""

import json
from typing import Sequence, cast

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.connections.models.conn_record import ConnRecord
from aries_cloudagent.core.profile import Profile, ProfileSession
from aries_cloudagent.messaging.responder import BaseResponder
from aries_cloudagent.resolver.base import (
    BaseDIDResolver,
    DIDMethodNotSupported,
    DIDNotFound,
    ResolverType,
)
from aries_cloudagent.storage.base import BaseStorage
from pydid import DID, DIDDocument

from .acapy_tools.awaitable_handler import send_and_wait_for_response
from .protocol.v0_9 import ResolveDID, ResolveDIDResult


class DIDCommResolver(BaseDIDResolver):
    """Universal DID Resolver with DIDCOMM messages."""

    METADATA_KEY = "didcomm_resolver"
    METADATA_METHODS = "methods"

    def __init__(self, conn_id: str, methods: Sequence[str]):
        """Initialize DIDCommResolver."""
        super().__init__(ResolverType.NON_NATIVE)
        self.connection_id = conn_id
        self._supported_methods = methods

    async def setup(self, context: InjectionContext):
        """Empty, setup is done at registration of connection as resolver."""

    @property
    def supported_methods(self) -> Sequence[str]:
        """Return supported methods.

        By determining methods from config file, we preserve the ability to not
        use the universal resolver for a given method, even if the universal
        is capable of resolving that method.
        """
        return self._supported_methods

    @classmethod
    async def register_connection(
        cls,
        session: ProfileSession,
        connection_id: str,
        methods: Sequence[str],
    ):
        """Register connection as a resolver connection."""
        conn_record = await ConnRecord.retrieve_by_id(session, connection_id)
        conn_record = cast(ConnRecord, conn_record)
        await conn_record.metadata_set(
            session, cls.METADATA_KEY, {cls.METADATA_METHODS: methods}
        )

    async def _resolve(self, profile: Profile, did: DID) -> DIDDocument:
        """Resolve DID through remote universal resolver."""
        async with profile.session() as session:
            storage = session.inject(BaseStorage)

            records = await storage.find_all_records(
                ConnRecord.RECORD_TYPE_METADATA, {"key": self.METADATA_KEY}
            )
            filtered_records = [
                record
                for record in records or []
                if did.method in json.loads(record.value)["methods"]
            ]
            connection_ids = [
                record.tags["connection_id"] for record in filtered_records
            ]

            if not connection_ids:
                raise DIDMethodNotSupported(
                    f'No connection configured to resolve method "{did.method}"'
                )

            responder = session.inject(BaseResponder)
            assert responder
            for conn_id in connection_ids:
                # Construct Resolve DID message
                resolve_did_message = ResolveDID(did=str(did))

                try:
                    response = await send_and_wait_for_response(
                        message=resolve_did_message,
                        response_type=ResolveDIDResult,
                        responder=responder,
                        connection_id=conn_id,
                    )
                    return DIDDocument.deserialize(response.did_document)
                except DIDNotFound:
                    continue

            raise DIDNotFound("DID not found on any resolver connections")
