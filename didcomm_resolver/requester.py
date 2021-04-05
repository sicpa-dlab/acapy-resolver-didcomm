"""
Setup requester capabilities for DIDComm Resolver protocol handlers and
register a DIDCommResolver to the DIDResolverRegistry.
"""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.resolver.did_resolver_registry import DIDResolverRegistry
from .resolver import DIDCommResolver


async def setup(context: InjectionContext):
    """Setup requester capabilities."""
    registry = context.inject(DIDResolverRegistry)
    registry.register(DIDCommResolver())
