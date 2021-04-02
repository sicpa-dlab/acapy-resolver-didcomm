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

class DIDCommResolver(BaseDIDResolver):
    """Universal DID Resolver with DIDCOMM messages."""
    METADATA_KEY = "didcomm_resolver"
    def __init__(self,conn_id: str, methods: Sequence[str]):
        """Initialize DIDCommResolver."""
        super().__init__(ResolverType.NON_NATIVE)
        self.connection_id = conn_id
        self._supported_methods = methods

    async def setup(self, context: InjectionContext):
        """empty, setup is done at registration of connection as resolver."""

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
            metadata = map(lambda record: record,
                await storage.find_all_records(
                    ConnRecord.RECORD_TYPE_METADATA, {'key': self.METADATA_KEY}
                )
            )
            admins = [
                await ConnRecord.retrieve_by_id(session, id)
                for id in admin_ids
            ]
            for conn in records:
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
