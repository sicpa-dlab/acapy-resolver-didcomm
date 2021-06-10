"""DIDComm Resovler plugin for ACA-Py; requester role."""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.core.protocol_registry import ProtocolRegistry
from aries_cloudagent.resolver.did_resolver_registry import DIDResolverRegistry

from didcomm_resolver.protocol.v0_9 import ResolveDIDProblemReport, ResolveDIDResult

from ...resolver import DIDCommResolver
import yaml

__all__ = ["setup"]

CONFIG_FILE = "didcomm_resolver/default_config.yml"


async def setup(context: InjectionContext):
    """Setup requester capabilities."""

    conf = context.settings.get("plugin_config", {}).get("didcomm_resolver.role.requester")
    if conf:
        with open(CONFIG_FILE, "r") as default_config:
            config = yaml.safe_load(default_config)

        methods = conf.get("methods")
        if methods:
            config["methods"] = methods

        with open(CONFIG_FILE, "w") as default_config:
            default_config.write(yaml.safe_dump(config))

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
