"""Test AwaitableHandler classes."""


from unittest.mock import MagicMock

from aiohttp import web
from aries_cloudagent.admin.request_context import AdminRequestContext
from aries_cloudagent.connections.models.conn_record import ConnRecord
from aries_cloudagent.messaging.models.base import BaseModelError
from aries_cloudagent.storage.error import StorageError, StorageNotFoundError
from asynctest import mock
import pytest

from didcomm_resolver.resolver import ResolverConnection
from didcomm_resolver.role.requester.routes import (
    connection,
    connection_register,
    connection_remove,
    connection_update,
    connections,
    post_process_routes,
    register,
)


TEST_RESOLVER_CONNECTIONS = [ResolverConnection("test-1", {"test", "example"})]


@pytest.fixture
def context():
    """Context fixture."""
    yield AdminRequestContext.test_context()


@pytest.fixture
def web_request(context):
    """Web request fixture."""
    request_dict = {
        "context": context,
        "outbound_message_router": mock.CoroutineMock(),
    }
    request = mock.MagicMock(
        app={},
        match_info={},
        query={},
        json=mock.CoroutineMock(),
        __getitem__=lambda _, k: request_dict[k],
    )
    yield request


@pytest.fixture
def conn_record():
    """Connection record fixture."""
    record = ConnRecord()
    record.metadata_get = mock.CoroutineMock(return_value={"methods": "test"})
    record.metadata_set = mock.CoroutineMock()
    record.metadata_delete = mock.CoroutineMock()
    yield record


@pytest.fixture(autouse=True)
def MockConnRecord(conn_record):
    """Mock ConnRecord fixture."""
    with mock.patch("didcomm_resolver.resolver.ConnRecord") as patched:
        patched.retrieve_by_id = mock.CoroutineMock(return_value=conn_record)
        yield patched


@pytest.fixture(autouse=True)
def mock_resolver_connections():
    """Mock DIDCommResolver.resolver_connections."""
    with mock.patch(
        "didcomm_resolver.resolver.DIDCommResolver.resolver_connections",
        mock.CoroutineMock(return_value=TEST_RESOLVER_CONNECTIONS),
    ) as patched:
        yield patched


@pytest.mark.asyncio
async def test_connection(web_request):
    web_request.match_info = {"conn_id": "mocked_id"}
    result = await connection(web_request)
    assert result.reason == "OK"
    assert result.status == 200


@pytest.mark.asyncio
async def test_connection_x(web_request, MockConnRecord):
    MockConnRecord.retrieve_by_id.side_effect = StorageError()
    web_request.match_info = {"conn_id": "mocked_id"}
    with pytest.raises(web.HTTPBadRequest):
        await connection(web_request)


@pytest.mark.asyncio
async def test_connections(web_request):
    result = await connections(web_request)
    assert result.reason == "OK"
    assert result.status == 200


@pytest.mark.asyncio
async def test_connections_x(mock_resolver_connections, web_request):
    mock_resolver_connections.side_effect = StorageError()
    with pytest.raises(web.HTTPBadRequest):
        await connections(web_request)


@pytest.mark.asyncio
async def test_connection_register(web_request):
    web_request.match_info = {"conn_id": "test"}
    web_request.json.return_value = {"methods": ["test"]}
    result = await connection_register(web_request)
    assert result.reason == "OK"
    assert result.status == 200


@pytest.mark.asyncio
async def test_connection_register_x_no_such_connection(web_request, MockConnRecord):
    MockConnRecord.retrieve_by_id.side_effect = StorageNotFoundError()
    web_request.match_info = {"conn_id": "test"}
    web_request.json.return_value = {"methods": ["test"]}
    with pytest.raises(web.HTTPNotFound):
        await connection_register(web_request)


@pytest.mark.asyncio
async def test_connection_register_x_base_model_error(web_request, MockConnRecord):
    MockConnRecord.retrieve_by_id.side_effect = BaseModelError()
    web_request.match_info = {"conn_id": "test"}
    web_request.json.return_value = {"methods": ["test"]}
    with pytest.raises(web.HTTPBadRequest):
        await connection_register(web_request)


@pytest.mark.asyncio
async def test_connection_update(web_request):
    web_request.match_info = {"conn_id": "test"}
    web_request.json.return_value = {"methods": ["test"]}
    result = await connection_update(web_request)
    assert result.reason == "OK"
    assert result.status == 200


@pytest.mark.asyncio
async def test_connection_update_x_no_such_connection(web_request, MockConnRecord):
    MockConnRecord.retrieve_by_id.side_effect = StorageNotFoundError()
    web_request.match_info = {"conn_id": "test"}
    web_request.json.return_value = {"methods": ["test"]}
    with pytest.raises(web.HTTPNotFound):
        await connection_update(web_request)


@pytest.mark.asyncio
async def test_connection_update_x_base_model_error(web_request, MockConnRecord):
    MockConnRecord.retrieve_by_id.side_effect = BaseModelError()
    web_request.match_info = {"conn_id": "test"}
    web_request.json.return_value = {"methods": ["test"]}
    with pytest.raises(web.HTTPBadRequest):
        await connection_update(web_request)


@pytest.mark.asyncio
async def test_connection_remove(web_request):
    web_request.match_info = {"conn_id": "test"}
    result = await connection_remove(web_request)
    assert result.reason == "OK"
    assert result.status == 200


@pytest.mark.asyncio
async def test_connection_remove_x_no_such_connection(web_request, MockConnRecord):
    MockConnRecord.retrieve_by_id.side_effect = StorageNotFoundError()
    web_request.match_info = {"conn_id": "test"}
    with pytest.raises(web.HTTPNotFound):
        await connection_remove(web_request)


@pytest.mark.asyncio
async def test_connection_remove_x_base_model_error(web_request, MockConnRecord):
    MockConnRecord.retrieve_by_id.side_effect = BaseModelError()
    web_request.match_info = {"conn_id": "test"}
    with pytest.raises(web.HTTPBadRequest):
        await connection_remove(web_request)


@pytest.mark.asyncio
async def test_register():
    await register(MagicMock())


@pytest.mark.asyncio
async def test_post_process_routes():
    post_process_routes(MagicMock())
