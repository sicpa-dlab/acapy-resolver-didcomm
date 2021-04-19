"""DIDComm Resolver Plugin for ACA-Py; resolver role."""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.core.protocol_registry import ProtocolRegistry
from ...protocol.v0_9 import ResolveDID

__all__ = ["setup"]


async def setup(context: InjectionContext):
    """Setup the plugin."""
    protocol_registry = context.inject(ProtocolRegistry)
    protocol_registry.register_message_types({ResolveDID.Meta.message_type: ResolveDID})
