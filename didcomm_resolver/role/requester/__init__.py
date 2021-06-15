"""DIDComm Resovler plugin for ACA-Py; requester role."""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.core.protocol_registry import ProtocolRegistry
from aries_cloudagent.resolver.did_resolver_registry import DIDResolverRegistry

from didcomm_resolver.protocol.v0_9 import ResolveDIDProblemReport, ResolveDIDResult

from ...resolver import DIDCommResolver

__all__ = ["setup"]


async def setup(context: InjectionContext):
    """Setup requester capabilities."""

    protocol_registry = context.inject(ProtocolRegistry)
    protocol_registry.register_message_types(
        {
            ResolveDIDResult.Meta.message_type: ResolveDIDResult,
            ResolveDIDProblemReport.Meta.message_type: ResolveDIDProblemReport,
        }
    )
    registry = context.inject(DIDResolverRegistry)
    resolver = DIDCommResolver()
    registry.register(resolver)
    await resolver.setup(context)
