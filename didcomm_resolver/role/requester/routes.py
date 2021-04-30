"""Routes for DIDComm Resolver."""
from typing import Set

from aiohttp import web
from aiohttp_apispec import docs, match_info_schema, request_schema, response_schema
from aries_cloudagent.admin.request_context import AdminRequestContext
from aries_cloudagent.messaging.models.base import BaseModelError
from aries_cloudagent.messaging.models.openapi import OpenAPISchema
from aries_cloudagent.messaging.valid import UUIDFour
from aries_cloudagent.storage.error import StorageError, StorageNotFoundError
from marshmallow import fields

from ...resolver import DIDCommResolver, ResolverConnection

DID_COMM_SPEC_URI = (
    "https://github.com/hyperledger/aries-rfcs/blob/master/"
    "features/0124-did-resolution-protocol/README.md"
)


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


class ConnectionRemoveResponseSchema(OpenAPISchema):
    """Result schema for connection register."""

    removed = fields.Str(description="Connection id of removed resolver.")


class ResolverConnectionSchema(OpenAPISchema):
    """Result schema for resolver connection metadata."""

    connection_id = fields.Str()
    methods = fields.List(fields.Str())


class ResolverConnectionListSchema(OpenAPISchema):
    """Result schema for list of connection ids."""

    results = fields.List(
        fields.Nested(ResolverConnectionSchema),
        description="List of connections registered as did resolvers.",
    )


@docs(
    tags=["didcomm-resolver"],
    summary="List DIDcomm resolvers.",
)
@response_schema(ResolverConnectionListSchema(), 200, description="")
async def connections(request: web.Request):
    """
    Request handler for listing resolver connections.

    Args:
        request: aiohttp request object

    Returns:
        The connection list response

    """
    context: AdminRequestContext = request["context"]
    async with context.session() as session:
        try:
            resolver_connections = await DIDCommResolver.resolver_connections(session)
        except (StorageError, BaseModelError) as err:
            raise web.HTTPBadRequest(reason=err.roll_up) from err

    return web.json_response(
        {
            "results": [
                resolver_connection.serialize()
                for resolver_connection in resolver_connections
            ]
        }
    )


@docs(
    tags=["didcomm-resolver"],
    summary="Fetch DIDComm Resolver details.",
)
@response_schema(ResolverConnectionSchema(), 200, description="")
async def connection(request: web.Request):
    """
    Request handler for listing a single DIDcomm resolver.

    Args:
        request: aiohttp request object

    Returns:
        The connection list response

    """
    context: AdminRequestContext = request["context"]
    connection_id = request.match_info["conn_id"]
    async with context.session() as session:
        try:
            resolver_connection = await ResolverConnection.from_connection_id(
                session, connection_id
            )
        except (StorageError, BaseModelError) as err:
            raise web.HTTPBadRequest(reason=err.roll_up) from err

    return web.json_response(resolver_connection.serialize())


@docs(tags=["didcomm-resolver"], summary="Register DIDcomm resolver.")
@match_info_schema(ConnIdMatchInfoSchema())
@request_schema(ConnectionRegisterRequestSchema())
@response_schema(ResolverConnectionSchema(), 200, description="")
async def connection_register(request: web.Request):
    """
    Request handler for registering a connection as a DIDcomm resolver.

    Args:
        request: aiohttp request object

    Returns:
        The connection list response

    """
    context: AdminRequestContext = request["context"]
    connection_id = request.match_info["conn_id"]
    body = await request.json() if request.body_exists else {}
    methods: Set[str] = body.get("methods", set())

    if not methods:
        raise web.HTTPBadRequest(reason="Methods must not be empty")

    async with context.session() as session:
        try:
            resolver_connection = await DIDCommResolver.set_resolver_connection(
                session, connection_id, methods
            )
        except StorageNotFoundError as err:
            raise web.HTTPNotFound(reason=err.roll_up) from err
        except BaseModelError as err:
            raise web.HTTPBadRequest(reason=err.roll_up) from err

    return web.json_response(resolver_connection.serialize())


@docs(tags=["didcomm-resolver"], summary="Update DIDcomm resolvable methods.")
@match_info_schema(ConnIdMatchInfoSchema())
@request_schema(ConnectionRegisterRequestSchema())
@response_schema(ResolverConnectionSchema(), 200, description="")
async def connection_update(request: web.Request):
    """
    Request handler for updating a DIDcomm resolver.

    Args:
        request: aiohttp request object

    Returns:
        The connection list response

    """
    return await connection_register(request)


@docs(tags=["didcomm-resolver"], summary="Remove an existing connection record.")
@match_info_schema(ConnIdMatchInfoSchema())
@response_schema(ConnectionRemoveResponseSchema, 200, description="")
async def connection_remove(request: web.Request):
    """
    Request handler for removing a DIDcomm resolver.

    Args:
        request: aiohttp request object
    """
    context: AdminRequestContext = request["context"]
    connection_id = request.match_info["conn_id"]

    async with context.session() as session:
        try:
            result = await DIDCommResolver.unset_resolver_connection(
                session, connection_id
            )
        except StorageNotFoundError as err:
            raise web.HTTPNotFound(reason=err.roll_up) from err
        except BaseModelError as err:
            raise web.HTTPBadRequest(reason=err.roll_up) from err
    return web.json_response({"removed": result})


async def register(app: web.Application):
    """Register routes."""

    app.add_routes(
        [
            web.get("/resolver/connections", connections, allow_head=False),
            web.get("/resolver/connections/{conn_id}", connection, allow_head=False),
            web.post("/resolver/register/{conn_id}", connection_register),
            web.post("/resolver/update/{conn_id}", connection_update),
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
            "name": "DIDcomm-resolver",
            "description": "Resolver Connection Manager",
            "externalDocs": {"description": "Specification", "url": DID_COMM_SPEC_URI},
        }
    )
