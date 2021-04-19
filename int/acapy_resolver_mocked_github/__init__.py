"""DIDCOMM Universal Resolver Plugin for ACA-Py With Mocked GITHUB Methods"""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.resolver.did_resolver_registry import DIDResolverRegistry
from .resolver import DIDCommResolver
from .resolver_mock import GithubResolver

__all__ = ["DIDCommResolver"]


async def setup(context: InjectionContext):
    """Setup the plugin."""
    registry = context.inject(DIDResolverRegistry)
    registry.register(DIDCommResolver())

    # Setup the Github resolver mock
    registry = context.inject(DIDResolverRegistry)
    assert isinstance(registry, DIDResolverRegistry)
    registry.register(GithubResolver())
