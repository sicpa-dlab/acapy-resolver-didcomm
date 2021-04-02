"""DIDCOMM Universal Resolver Plugin for ACA-Py"""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.resolver.did_resolver_registry import DIDResolverRegistry
from aries_cloudagent.connections.models import ConnRecord
from .resolver import DIDCommResolver

__all__ = ["DIDCommResolver"]


async def setup(context: InjectionContext):
    """Setup the plugin."""
    registry = context.inject(DIDResolverRegistry)
    # TODO:
    # get session for storage
    session = (
        registry.get_session()
    )  # FIXME: find magic to get session before its created
    # get all connection records metadata
    records = await ConnRecord.query(session, {}, alt=True)
    results = [record.serialize() for record in records]
    # if resolver, create didcomm_resolver
    for conn in results:
        record = await ConnRecord.retrieve_by_id(session, conn.connection_id)
        metadata = await record.metadata_get(session, "didcomm_resolver")
        resolver = DIDCommResolver(conn.connection_id, metadata.get("methods"))
        registry.register(resolver)
