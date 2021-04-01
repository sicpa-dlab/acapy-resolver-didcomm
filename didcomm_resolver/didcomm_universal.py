"""Didcommm Universal DID Resolver."""

import os
from asyncio import Future
from pathlib import Path
from typing import Sequence

import yaml
from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.connections.models.conn_record import ConnRecord
from aries_cloudagent.core.profile import Profile
from aries_cloudagent.messaging.responder import BaseResponder
from aries_cloudagent.resolver.base import BaseDIDResolver, ResolverError, ResolverType
from aries_cloudagent.storage.base import BaseStorage
from pydid import DID, DIDDocument

from .protocol.v0_9 import ResolveDID, ResolveDIDResult


class DIDCommUniversalDIDResolver(BaseDIDResolver):
    """Universal DID Resolver with DIDCOMM messages."""

    def __init__(self):
        """Initialize DIDCommUniversalDIDResolver."""
        super().__init__(ResolverType.NON_NATIVE)
        self._endpoint: str = ""
        self._supported_methods: Sequence[str] = [""]

    async def setup(self, context: InjectionContext):
        """Preform setup, populate supported method list, configuration."""
        config_file = os.environ.get(
            "UNI_RESOLVER_CONFIG", Path(__file__).parent / "default_config.yml"
        )
        try:
            with open(config_file) as input_yaml:
                configuration = yaml.load(input_yaml, Loader=yaml.SafeLoader)
        except FileNotFoundError as err:
            raise ResolverError(
                f"Failed to load configuration file for {self.__class__.__name__}"
            ) from err
        assert isinstance(configuration, dict)
        self.configure(configuration)

    def configure(self, configuration: dict):
        """Configure this instance of the resolver from configuration dict."""
        try:
            self._endpoint = configuration["endpoint"]
            self._supported_methods = configuration["methods"]
        except KeyError as err:
            raise ResolverError(
                f"Failed to configure {self.__class__.__name__}, "
                "missing attribute in configuration: {err}"
            ) from err

    @property
    def supported_methods(self) -> Sequence[str]:
        """Return supported methods.

        By determining methods from config file, we preserve the ability to not
        use the universal resolver for a given method, even if the universal
        is capable of resolving that method.
        """
        return self._supported_methods

    async def _resolve(self, profile: Profile, did: DID) -> DIDDocument:
        """Resolve DID through remote universal resolver."""
        # Look up resolver connection using meta data on connection
        async with profile.session() as session:
            storage = session.inject(BaseStorage)
            meta_data_records = await storage.find_all_records(
                ConnRecord.RECORD_TYPE_METADATA,
                {"key": "didcomm_resolver"},  # TODO: update name to be generalized
            )
            if meta_data_records:
                conn_id = meta_data_records[0].tags["connection_id"]
                # Construct Resolve DID message
                resolved_did_message = ResolveDID(did=did)
                # Get handle to response
                response_handle: Future = ResolveDIDResult.Handler.response_to(
                    resolved_did_message
                )
                # Send message to the resolver connection
                responder = session.inject(BaseResponder, required=False)
                await responder.send(resolved_did_message, connection_id=conn_id)
                response = await response_handle
                return response.did_document
            else:
                raise ResolverError("no connection configured for resolver!")
