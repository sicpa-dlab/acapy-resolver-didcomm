"""Mock Resolver."""

from typing import Sequence

from aries_cloudagent.core.profile import Profile
from aries_cloudagent.resolver.base import (
    BaseDIDResolver,
    DIDNotFound,
    ResolverType,
)
from pydid import DID


class MockResolver(BaseDIDResolver):
    """Mock Resolver."""

    def __init__(self):
        super().__init__(ResolverType.NATIVE)

    @property
    def supported_methods(self) -> Sequence[str]:
        """Return list of supported methods."""
        return ["mock"]

    async def setup(self, context):
        """Setup the mock resolver (none required)."""

    async def _resolve(self, profile: Profile, did: str) -> dict:
        """Resolve mock DIDs."""
        as_did = DID(did)
        # Document found: as_did.method_specific_id == "test"
        # Document not found: as_did.method_specific_id != "test"
        if as_did.method_specific_id == "test":
            return {
                "id": "did:mock:test:mocked_id",
                "@context": "https://www.w3.org/ns/did/v1",
            }

        raise DIDNotFound(f"No document found for {did}")
