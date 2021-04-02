
import json

from aiohttp import web
from aiohttp_apispec import (
    docs,
    match_info_schema,
    querystring_schema,
    request_schema,
    response_schema,
)

from marshmallow import fields, validate, validates_schema

from aries_cloudagent.admin.request_context import AdminRequestContext
from aries_cloudagent.connections.models.conn_record import ConnRecord, ConnRecordSchema
from aries_cloudagent.messaging.models.base import BaseModelError
from aries_cloudagent.messaging.models.openapi import OpenAPISchema
from aries_cloudagent.messaging.valid import (
    ENDPOINT,
    INDY_DID,
    INDY_RAW_PUBLIC_KEY,
    UUIDFour,
)
from aries_cloudagent.storage.error import StorageError, StorageNotFoundError
from aries_cloudagent.wallet.error import WalletError
from aries_cloudagent.resolver import DIDResolverRegistry
from .didcomm_universal import DIDCommResolver
DID_COMM_SPEC_URI = ""  # FIXME: PLS


class ConnIdMatchInfoSchema(OpenAPISchema):
    """Path parameters and validators for request taking connection id."""

    conn_id = fields.Str(
        description="Connection identifier", required=True, example=UUIDFour.EXAMPLE
    )


class ConnectionRegisterRequestSchema(OpenAPISchema):
    """Request schema for connection registering."""

    methods = fields.List(
        fields.Str(description="Did method."),
        description="List of supported did methods.",
    )


class ConnectionRegisterResultSchema(OpenAPISchema):
    """Result schema for connection register."""

    fields.Str(description="Connection id of registered resolver.")


class ConnectionListSchema(OpenAPISchema):
    """Result schema for connection metadata."""

    fields.List(
        fields.Str(description="connection id"), description="List of connections registered as did resolvers."
    )

@docs(
    tags=["resolver"],
    summary="get a list of resolver connections.",
)
@response_schema(ConnectionListSchema(), 200, description="")
async def connections(request: web.BaseRequest):
    """
    Request handler for listing resolver connections.

    Args:
        request: aiohttp request object

    Returns:
        The connection list response

    """
    context: AdminRequestContext = request["context"]

    tag_filter = {}
    post_filter = {}
    session = await context.session()
    def connection_sort_key(conn):
        """Get the sorting key for a particular connection."""

        conn_rec_state = ConnRecord.State.get(conn["state"])
        if conn_rec_state is ConnRecord.State.ABANDONED:
            pfx = "2"
        elif conn_rec_state is ConnRecord.State.INVITATION:
            pfx = "1"
        else:
            pfx = "0"

        return pfx + conn["created_at"]
    try:
        # TODO: implement
        # search metadata records for resolvers
        records = await ConnRecord.query(
            session, tag_filter, post_filter_positive=post_filter, alt=True
        )
        results = [record.serialize() for record in records]
        results.sort(key=connection_sort_key)
        resolvers = []
        for conn in results:
            record = await ConnRecord.retrieve_by_id(session, conn.connection_id)
            resolvers.append(await record.metadata_get(session, "didcomm_resolver"))
        # reduce metadata records into a list of conn_id
        # TODO: reduce
    except (StorageError, BaseModelError) as err:
        raise web.HTTPBadRequest(reason=err.roll_up) from err

    return web.json_response(resolvers)


@docs(tags=["resolver"], summary="Register connection as a new resolver.")
@match_info_schema(ConnIdMatchInfoSchema())
@request_schema(ConnectionRegisterRequestSchema())
@response_schema(ConnectionRegisterResultSchema(), 200, description="")
async def connection_register(request: web.BaseRequest):
    context: AdminRequestContext = request["context"]
    session = await context.session()
    connection_id = request.match_info["conn_id"]
    body = await request.json() if request.body_exists else {}
    methods = body.get("methods")
    try:
        registry: DIDResolverRegistry = session.inject(DIDResolverRegistry)
        resolver = DIDCommResolver(supported_methods=methods)
        registry.register(resolver)
    except Exception as err:
        raise web.HTTPBadRequest(reason=err.roll_up) from err

    return web.json_response({connection_id:methods})


async def register(app: web.Application):
    """Register routes."""

    app.add_routes(
        [
            web.get("/resolver/connections", connections, allow_head=False),
            web.get("/resolver/connections/{conn_id}", connection, allow_head=False),
            web.post("/resolver/register/{conn_id}", connection_register),
            web.delete("/resolver/connections/{conn_id}", connection_remove),
        ]
    )



def post_process_routes(app: web.Application):
    """Amend swagger API."""

    # Add top-level tags description
    if "tags" not in app._state["swagger_dict"]:
        app._state["swagger_dict"]["tags"] = []
    app._state["swagger_dict"]["tags"].append(
        {
            "name": "connection",
            "description": "Connection management",
            "externalDocs": {"description": "Specification", "url": DID_COMM_SPEC_URI},
        }
    )