"""DIDCOMM Universal Resolver Plugin for ACA-Py"""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.resolver.did_resolver_registry import DIDResolverRegistry

from .did_comm_universal import DIDCommUniversalDIDResolver


async def setup(context: InjectionContext):
    """Setup the plugin."""
    registry = context.inject(DIDResolverRegistry)
    resolver = DIDCommUniversalDIDResolver()
    await resolver.setup(context)
    registry.register(resolver)
