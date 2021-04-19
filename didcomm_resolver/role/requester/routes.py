"""Routes for DIDComm Resolver."""
import json
from aiohttp import web
from aiohttp_apispec import (
    docs,
    match_info_schema,
    request_schema,
    response_schema,
)
from typing import Sequence

from marshmallow import fields

# , validate, validates_schema

from aries_cloudagent.admin.request_context import AdminRequestContext
from aries_cloudagent.connections.models.conn_record import ConnRecord
from aries_cloudagent.messaging.models.base import BaseModelError
from aries_cloudagent.messaging.models.openapi import OpenAPISchema
from aries_cloudagent.messaging.valid import UUIDFour
from aries_cloudagent.storage.error import StorageError, StorageNotFoundError
from ...resolver import DIDCommResolver

DID_COMM_SPEC_URI = ""  # FIXME: PLS
METADATA_KEY = DIDCommResolver.METADATA_KEY


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


class ConnectionRemoveResponseSchema(OpenAPISchema):
    """Result schema for connection register."""

    fields.Str(description="Connection id of removed resolver.")


class ConnectionIDListSchema(OpenAPISchema):
    """Result schema for list of connection ids."""

    fields.List(
        fields.Str(description="connection id"),
        description="List of connections registered as did resolvers.",
    )


class ConnectionResolverMetadataSchema(OpenAPISchema):
    """Result schema for resolver connection metadata."""

    connection_id = fields.Str()
    methods = fields.List(fields.Str())
    state = fields.Str()


@docs(
    tags=["resolver"],
    summary="get a list of resolver connections.",
)
@response_schema(ConnectionIDListSchema(), 200, description="")
async def connections(request: web.BaseRequest):
    """
    Request handler for listing resolver connections.

    Args:
        request: aiohttp request object

    Returns:
        The connection list response

    """
    context: AdminRequestContext = request["context"]
    session = await context.session()

    def connection_sort_key(conn_metadata):
        """Get the sorting key for a particular connection."""
        conn, _ = conn_metadata
        conn_rec_state = ConnRecord.State.get(conn.state)
        if conn_rec_state is ConnRecord.State.ABANDONED:
            pfx = "2"
        elif conn_rec_state is ConnRecord.State.INVITATION:
            pfx = "1"
        else:
            pfx = "0"
        return pfx + conn.created_at

    try:
        # search metadata records for resolvers
        records = await ConnRecord.query(session)
        resolvers_matadata = [
            (record, await record.metadata_get(session, METADATA_KEY))
            for record in records
        ]
        # filter non resolver records
        resolvers_matadata = [
            (conn, metadata) for (conn, metadata) in resolvers_matadata if metadata
        ]
        # sort by connection state
        resolvers_matadata.sort(key=connection_sort_key)
        # prepare results with relevant information
        results = []
        for (conn, metadata) in resolvers_matadata:

            if not isinstance(metadata, dict):
                value = json.loads(metadata.value)
            else:
                value = metadata
            results.append(
                {
                    "connection_id": conn.connection_id,
                    "methods": value["methods"],
                    "state": conn.state,
                }
            )
    except (StorageError, BaseModelError) as err:
        raise web.HTTPBadRequest(reason=err.roll_up) from err

    return web.json_response(results)


@docs(
    tags=["resolver"],
    summary="get resolver connection details.",
)
@response_schema(ConnectionIDListSchema(), 200, description="")
async def connection(request: web.BaseRequest):
    """
    Request handler for listing a single resolver connection.

    Args:
        request: aiohttp request object

    Returns:
        The connection list response

    """
    context: AdminRequestContext = request["context"]
    connection_id = request.match_info["conn_id"]
    session = await context.session()
    try:
        record = await ConnRecord.retrieve_by_id(session, connection_id)
        metadata = await record.metadata_get(session, METADATA_KEY)
        if not isinstance(metadata, dict):
            metadata = json.loads(metadata.value)
        methods = [] if metadata is None else metadata["methods"]
        resolver = {
            "connection_id": record.connection_id,
            "methods": methods,
            "state": record.state,
        }
    except (StorageError, BaseModelError) as err:
        raise web.HTTPBadRequest(reason=err.roll_up) from err

    return web.json_response(resolver)


@docs(tags=["resolver"], summary="Register connection as a new resolver.")
@match_info_schema(ConnIdMatchInfoSchema())
@request_schema(ConnectionRegisterRequestSchema())
@response_schema(ConnectionRegisterResultSchema(), 200, description="")
async def connection_register(request: web.BaseRequest):
    context: AdminRequestContext = request["context"]
    session = await context.session()
    connection_id = request.match_info.get("conn_id")
    body = await request.json() if request.body_exists else {}
    methods: Sequence[str] = body.get("methods", [])
    try:
        results = await DIDCommResolver.register_connection(
            session, connection_id, methods
        )
    except StorageNotFoundError as err:
        raise web.HTTPNotFound(reason=err.roll_up) from err
    except BaseModelError as err:
        raise web.HTTPBadRequest(reason=err.roll_up) from err
    return web.json_response({"results": results})


@docs(tags=["resolver"], summary="Update connection methods that are resolvable.")
@match_info_schema(ConnIdMatchInfoSchema())
@request_schema(ConnectionRegisterRequestSchema())
@response_schema(ConnectionRegisterResultSchema(), 200, description="")
async def connection_update(request: web.BaseRequest):
    context: AdminRequestContext = request["context"]
    session = await context.session()
    connection_id = request.match_info.get("conn_id")
    body = await request.json() if request.body_exists else {}
    methods: Sequence[str] = body.get("methods", [])
    try:
        await DIDCommResolver.update_connection(session, connection_id, methods)
    except StorageNotFoundError as err:
        raise web.HTTPNotFound(reason=err.roll_up) from err
    except BaseModelError as err:
        raise web.HTTPBadRequest(reason=err.roll_up) from err
    return web.json_response({"results": "Ok"})


@docs(tags=["connection"], summary="Remove an existing connection record")
@match_info_schema(ConnIdMatchInfoSchema())
@response_schema(ConnectionRemoveResponseSchema, 200, description="")
async def connection_remove(request: web.BaseRequest):
    """
    Request handler for removing a connection record.

    Args:
        request: aiohttp request object
    """
    context: AdminRequestContext = request["context"]
    connection_id = request.match_info.get("conn_id")
    session = await context.session()
    try:
        results = await DIDCommResolver.remove_connection(session, connection_id)
    except StorageNotFoundError as err:
        raise web.HTTPNotFound(reason=err.roll_up) from err
    except BaseModelError as err:
        raise web.HTTPBadRequest(reason=err.roll_up) from err
    return web.json_response({"results": results})


async def register(app: web.Application):
    """Register routes."""

    app.add_routes(
        [
            # Listing resolver connections
            web.get("/resolver/connections", connections, allow_head=False),
            # Retrieving details for a single resolver connection
            web.get("/resolver/connections/{conn_id}", connection, allow_head=False),
            # Registering a connection as a resolver
            web.post("/resolver/register/{conn_id}", connection_register),
            web.post("/resolver/update/{conn_id}", connection_update),
            # Removing a connection as a resolver
            web.delete("/resolver/connections/{conn_id}", connection_remove),
            # TODO: add support for future rfc for requesting resolving service
        ]
    )


def post_process_routes(app: web.Application):
    """Amend swagger API."""

    # Add top-level tags description
    if "tags" not in app._state["swagger_dict"]:
        app._state["swagger_dict"]["tags"] = []
    app._state["swagger_dict"]["tags"].append(
        {
            "name": "resolver-connection",
            "description": "Resolver Connection Manager",
            "externalDocs": {"description": "Specification", "url": DID_COMM_SPEC_URI},
        }
    )
