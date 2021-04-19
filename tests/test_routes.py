"""Test AwaitableHandler classes."""


from unittest.mock import MagicMock
from aiohttp import web
from aries_cloudagent.messaging.models.base import BaseModelError

from didcomm_resolver.routes import (
    connections,
    connection,
    connection_register,
    connection_remove,
    register,
    post_process_routes, connection_update,
)
import pytest
from asynctest import mock
from aries_cloudagent.storage.error import StorageError, StorageNotFoundError


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.ConnRecord")
async def test_connection(conRecord_mock):
    async_mock = AsyncMock()
    async_mock.metadata_get.return_value = {"methods": "test"}
    async_mock.connection_id = "conn"
    async_mock.state = "active"

    async def list_aux(*args, **kwargs):
        return async_mock

    conRecord_mock.retrieve_by_id = list_aux

    context_magic = MagicMock()
    context_magic.session.side_effect = AsyncMock()
    request = web.BaseRequest
    request.match_info = {"conn_id": "mocked_id"}
    #{"context": context_magic}

    request = MagicMock()
    request["context"].session.side_effect = list_aux

    result = await connection(request)
    assert result.reason == "OK"
    assert result.status == 200


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.ConnRecord")
async def test_connection_fail(conRecord_mock):
    async_mock = AsyncMock()
    async_mock.metadata_get.return_value = {"methods": "test"}
    async_mock.connection_id = "conn"
    async_mock.state = "active"

    async def list_aux(*args, **kwargs):
        return async_mock

    async def raise_aux(*args, **kwargs):
        raise StorageError()

    conRecord_mock.retrieve_by_id = raise_aux

    context_magic = MagicMock()
    context_magic.session.side_effect = AsyncMock()
    request = web.BaseRequest
    request.match_info = {"conn_id": "mocked_id"}
    request = MagicMock()
    request["context"].session.side_effect = list_aux

    with pytest.raises(web.HTTPBadRequest):
        await connection(request)



@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.ConnRecord")
async def test_send_and_wait_for_response(conRecord_mock):
    async_mock = AsyncMock()
    async_mock.metadata_get.return_value = {"methods": "test"}
    async_mock.connection_id = "conn"
    async_mock.state = "active"

    async def list_aux(*args, **kwargs):
        return [async_mock]

    conRecord_mock.query.side_effect = list_aux

    context_magic = MagicMock()
    context_magic.session.side_effect = AsyncMock()
    result = await connections({"context": context_magic})
    assert result.reason == "OK"
    assert result.status == 200


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.ConnRecord")
async def test_send_and_wait_for_response_fail(conRecord_mock):
    async def list_aux(*args, **kwargs):
        raise StorageError()


    conRecord_mock.retrieve_by_id.side_effect = StorageError
    conRecord_mock.query.side_effect = list_aux

    with pytest.raises(web.HTTPBadRequest):
        await connections({"context": AsyncMock()})


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.DIDCommResolver")
async def test_connection_register(DIDCommResolver_mock):

    async def aux(*args):
        return []
    DIDCommResolver_mock.register_connection.side_effect = aux
    async_mock = AsyncMock()
    async_mock.session.return_value = MagicMock()

    my_dict = {"context": async_mock, "conn_id": "123", "c": 3}

    def getitem(name):
        return my_dict[name]

    def setitem(name, val):
        my_dict[name] = val

    mock = MagicMock()
    mock.__getitem__.side_effect = getitem
    mock.__setitem__.side_effect = setitem

    mock.match_info = mock
    mock.body_exists = False
    result = await connection_register(mock)
    assert result.reason == "OK"
    assert result.status == 200

@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.DIDCommResolver")
async def test_connection_register_fail(DIDCommResolver_mock):

    async def aux(*args):
        raise BaseModelError()
    DIDCommResolver_mock.register_connection.side_effect = aux
    async_mock = AsyncMock()
    async_mock.session.return_value = MagicMock()

    my_dict = {"context": async_mock, "conn_id": "123", "c": 3}

    def getitem(name):
        return my_dict[name]

    def setitem(name, val):
        my_dict[name] = val

    mock = MagicMock()
    mock.__getitem__.side_effect = getitem
    mock.__setitem__.side_effect = setitem

    mock.match_info = mock
    mock.body_exists = False
    with pytest.raises(web.HTTPBadRequest):
        await connection_register(mock)


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.DIDCommResolver")
async def test_connection_update(DIDCommResolver_mock):

    async def aux(*args):
        return []

    DIDCommResolver_mock.update_connection.side_effect = aux
    async_mock = AsyncMock()
    async_mock.session.return_value = MagicMock()

    my_dict = {"context": async_mock, "conn_id": "123", "c": 3}

    def getitem(name):
        return my_dict[name]

    def setitem(name, val):
        my_dict[name] = val

    mock = MagicMock()
    mock.__getitem__.side_effect = getitem
    mock.__setitem__.side_effect = setitem

    mock.match_info = mock
    mock.body_exists = False
    result = await connection_update(mock)
    assert result.reason == "OK"
    assert result.status == 200


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.DIDCommResolver")
async def test_connection_update_fail(DIDCommResolver_mock):

    async def raise_exc(*args):
        raise BaseModelError()

    DIDCommResolver_mock.update_connection.side_effect = raise_exc
    async_mock = AsyncMock()
    async_mock.session.return_value = MagicMock()

    my_dict = {"context": async_mock, "conn_id": "123", "c": 3}

    def getitem(name):
        return my_dict[name]

    def setitem(name, val):
        my_dict[name] = val

    mock = MagicMock()
    mock.__getitem__.side_effect = getitem
    mock.__setitem__.side_effect = setitem

    mock.match_info = mock
    mock.body_exists = False
    with pytest.raises(web.HTTPBadRequest):
        await connection_update(mock)


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.DIDCommResolver")
async def test_remove_connection(DIDCommResolver_mock):

    async def aux(*args):
        return []

    DIDCommResolver_mock.remove_connection.side_effect = aux
    async_mock = AsyncMock()
    async_mock.session.return_value = MagicMock()

    my_dict = {"context": async_mock, "conn_id": "123", "c": 3}

    def getitem(name):
        return my_dict[name]

    def setitem(name, val):
        my_dict[name] = val

    mock = MagicMock()
    mock.__getitem__.side_effect = getitem
    mock.__setitem__.side_effect = setitem

    mock.match_info = mock
    mock.body_exists = False
    result = await connection_remove(mock)
    assert result.reason == "OK"
    assert result.status == 200


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.DIDCommResolver")
async def test_remove_connection_fail(DIDCommResolver_mock):

    async def aux(*args):
        raise BaseModelError()

    DIDCommResolver_mock.remove_connection.side_effect = aux
    async_mock = AsyncMock()
    async_mock.session.return_value = MagicMock()

    my_dict = {"context": async_mock, "conn_id": "123", "c": 3}

    def getitem(name):
        return my_dict[name]

    def setitem(name, val):
        my_dict[name] = val

    mock = MagicMock()
    mock.__getitem__.side_effect = getitem
    mock.__setitem__.side_effect = setitem

    mock.match_info = mock
    mock.body_exists = False
    with pytest.raises(web.HTTPBadRequest):
        await connection_remove(mock)


@pytest.mark.asyncio
async def test_register():
    await register(MagicMock())


@pytest.mark.asyncio
async def test_post_process_routes():
    post_process_routes(MagicMock())
