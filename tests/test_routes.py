"""Test AwaitableHandler classes."""


from unittest.mock import MagicMock
from aiohttp import web
from didcomm_resolver.routes import (
    connections,
    connection_register,
    register,
    post_process_routes,
)
import pytest
from asynctest import mock
from aries_cloudagent.storage.error import StorageError, StorageNotFoundError


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.ConnRecord")
async def test_send_and_wait_for_response(conRecord_mock):
    async def list_aux(*args, **kwargs):
        return [MagicMock()]

    async def aux(*args, **kwargs):
        result = AsyncMock()
        result.metadata_get.return_value = {"result": "test"}
        return result

    conRecord_mock.retrieve_by_id.side_effect = aux
    conRecord_mock.query.side_effect = list_aux

    result = await connections({"context": AsyncMock()})
    assert result.reason == "OK"
    assert result.status == 200


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.routes.ConnRecord")
async def test_send_and_wait_for_response_fail(conRecord_mock):
    async def list_aux(*args, **kwargs):
        return [MagicMock()]

    conRecord_mock.retrieve_by_id.side_effect = StorageError
    conRecord_mock.query.side_effect = list_aux

    with pytest.raises(web.HTTPBadRequest):
        await connections({"context": AsyncMock()})


@pytest.mark.asyncio
async def test_connection_register():
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
async def test_connection_register_fail():
    async_mock = AsyncMock()
    inject = MagicMock()
    inject.inject.side_effect = StorageNotFoundError
    async_mock.session.return_value = inject

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
async def test_register():
    await register(MagicMock())


@pytest.mark.asyncio
async def test_post_process_routes():
    post_process_routes(MagicMock())
