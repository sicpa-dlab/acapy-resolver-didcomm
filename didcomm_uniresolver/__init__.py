"""DIDCOMM Universal Resolver Plugin for ACA-Py"""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.resolver.did_resolver_registry import DIDResolverRegistry

from .didcomm_universal import DIDCommUniversalDIDResolver

__all__ = ["DIDCommUniversalDIDResolver"]


async def setup(context: InjectionContext):
    """Setup the plugin."""
    registry = context.inject(DIDResolverRegistry)
    resolver = DIDCommUniversalDIDResolver()
    await resolver.setup()
    registry.register(resolver)
