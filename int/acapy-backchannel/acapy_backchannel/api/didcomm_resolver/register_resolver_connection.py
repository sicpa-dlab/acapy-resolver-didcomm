from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.connection_register_request import ConnectionRegisterRequest
from ...models.resolver_connection import ResolverConnection
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    conn_id: str,
    json_body: ConnectionRegisterRequest,
) -> Dict[str, Any]:
    url = "{}/resolver/register/{conn_id}".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ResolverConnection]:
    if response.status_code == 200:
        response_200 = ResolverConnection.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ResolverConnection]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    conn_id: str,
    json_body: ConnectionRegisterRequest,
) -> Response[ResolverConnection]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    conn_id: str,
    json_body: ConnectionRegisterRequest,
) -> Optional[ResolverConnection]:
    """ """

    return sync_detailed(
        client=client,
        conn_id=conn_id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    conn_id: str,
    json_body: ConnectionRegisterRequest,
) -> Response[ResolverConnection]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    conn_id: str,
    json_body: ConnectionRegisterRequest,
) -> Optional[ResolverConnection]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            conn_id=conn_id,
            json_body=json_body,
        )
    ).parsed
