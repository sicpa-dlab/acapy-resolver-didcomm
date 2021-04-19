"""Mock Resolver setup."""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.resolver.did_resolver_registry import DIDResolverRegistry
from .mock_resolver import MockResolver

__all__ = ["MockResolver"]


async def setup(context: InjectionContext):
    """Setup the mock resolver."""
    print("FROM THE SETUP OF THE MOCK RESOLVER")
    registry = context.inject(DIDResolverRegistry)
    assert isinstance(registry, DIDResolverRegistry)
    registry.register(MockResolver())
    print(registry.resolvers)
