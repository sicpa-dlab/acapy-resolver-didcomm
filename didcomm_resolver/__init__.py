"""DIDCOMM Universal Resolver Plugin for ACA-Py"""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.resolver.did_resolver_registry import DIDResolverRegistry
from .resolver import DIDCommResolver

__all__ = ["DIDCommResolver"]


async def setup(context: InjectionContext):
    """Setup the plugin."""
    registry = context.inject(DIDResolverRegistry)
    registry.register(DIDCommResolver())
