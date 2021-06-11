"""Test universal resolver with did-comm messaging."""
# pylint: disable=redefined-outer-name,protected-access

from contextlib import contextmanager
import os
from unittest.mock import MagicMock

from aries_cloudagent.connections.models.conn_record import ConnRecord
from aries_cloudagent.core.in_memory import InMemoryProfile
from aries_cloudagent.messaging.request_context import RequestContext
from aries_cloudagent.messaging.responder import BaseResponder, MockResponder
from aries_cloudagent.resolver.base import (
    DIDMethodNotSupported,
    DIDNotFound,
    ResolverError,
)
from aries_cloudagent.storage.error import StorageNotFoundError
from asynctest import mock
import pytest
import json

from didcomm_resolver import DIDCommResolver
from didcomm_resolver.acapy_tools.awaitable_handler import WaitingForMessageFailed
from didcomm_resolver.protocol.v0_9 import ResolveDIDResult
from didcomm_resolver.resolver import ResolverConnection
from . import DOC


TEST_RESOLVER_CONNECTIONS = [ResolverConnection("test-1", {"test", "example"})]


@pytest.fixture
def resolver():
    """Resolver fixture."""
    didcomm_resolver = DIDCommResolver()
    didcomm_resolver.configure(
        {
            "endpoint": "https://example.com",
            "methods": ["example"],
        }
    )
    yield didcomm_resolver


@pytest.fixture
def profile():
    """Profile fixture."""
    yield InMemoryProfile.test_profile(bind={BaseResponder: MockResponder()})


@pytest.fixture
def context():
    yield RequestContext.test_context()


@pytest.fixture(autouse=True)
def mock_env():
    with mock.patch.dict(os.environ, {"UNI_RESOLVER_CONFIG": "fake_config"}):
        yield os.environ


@pytest.fixture()
def mock_config_file():
    @contextmanager
    def _mock_config_file(contents: str = None):
        if not contents:
            contents = json.load(
                {"endpoint": "http://example.com", "methods": ["example"]}
            )

        with mock.patch(
            "builtins.open",
            mock.mock_open(read_data=contents),
        ) as patched:
            yield patched

    yield _mock_config_file


@pytest.fixture
def response():
    """Response message fixture."""
    yield ResolveDIDResult(did_document=DOC)


@pytest.fixture
def conn_record():
    """Connection record fixture."""
    record = ConnRecord()
    record.metadata_get = mock.CoroutineMock(return_value={"methods": "test"})
    record.metadata_set = mock.CoroutineMock()
    record.metadata_delete = mock.CoroutineMock()
    yield record


@pytest.fixture
def MockConnRecord(conn_record):
    """Mock ConnRecord fixture."""
    with mock.patch("didcomm_resolver.resolver.ConnRecord") as patched:
        patched.retrieve_by_id = mock.CoroutineMock(return_value=conn_record)
        yield patched


@pytest.mark.asyncio
async def test_setup(mock_config_file, resolver, context):
    await resolver.setup(context)
    assert "sov" in resolver._supported_methods


@pytest.mark.asyncio
async def test_setup_failed(mock_config_file, resolver, context):
    with mock_config_file("fail"), pytest.raises(ResolverError):
        await resolver.setup(context)


@pytest.mark.asyncio
async def test_setup_plugin_config_error(mock_config_file, resolver, context):
    plug_conf = {"plugin_config": {"didcomm_resolver.role.requester": "error"}}
    context.update_settings(plug_conf)
    with pytest.raises(ResolverError):
        await resolver.setup(context)


@pytest.mark.asyncio
def test_supported_methods(resolver):
    assert resolver.supported_methods


@pytest.mark.asyncio
def test_configure_error(resolver):
    with pytest.raises(ResolverError):
        resolver.configure({"fake": "configure"})


@pytest.mark.asyncio
async def test_resolve_dict(resolver, profile, response):
    with mock.patch(
        "didcomm_resolver.resolver.send_and_wait_for_response",
        mock.CoroutineMock(return_value=response),
    ):
        with mock.patch(
            "didcomm_resolver.resolver.DIDCommResolver.resolver_connections",
            mock.CoroutineMock(return_value=TEST_RESOLVER_CONNECTIONS),
        ):
            result = await resolver._resolve(profile, "did:example:1234abcd")
            assert result == DOC


@pytest.mark.asyncio
async def test_resolve_not_found(resolver, profile):
    with mock.patch(
        "didcomm_resolver.resolver.DIDCommResolver.resolver_connections",
        mock.CoroutineMock(return_value=TEST_RESOLVER_CONNECTIONS),
    ):
        with mock.patch(
            "didcomm_resolver.resolver.send_and_wait_for_response",
            mock.CoroutineMock(side_effect=DIDNotFound),
        ), pytest.raises(DIDNotFound):
            await resolver._resolve(profile, "did:example:1234abcd")


@pytest.mark.asyncio
async def test_resolve_timeout(resolver, profile):
    with mock.patch(
        "didcomm_resolver.resolver.DIDCommResolver.resolver_connections",
        mock.CoroutineMock(return_value=TEST_RESOLVER_CONNECTIONS),
    ):
        with mock.patch(
            "didcomm_resolver.resolver.send_and_wait_for_response",
            mock.CoroutineMock(side_effect=WaitingForMessageFailed),
        ), pytest.raises(DIDNotFound):
            await resolver._resolve(profile, "did:example:1234abcd")


@pytest.mark.asyncio
async def test_resolve_no_responder(resolver, profile):
    profile.context.injector.bind_instance(BaseResponder, False)
    with pytest.raises(ValueError):
        await resolver._resolve(profile, "did:example:1234abcd")


@pytest.mark.asyncio
async def test_resolve_not_supported(resolver, profile):
    with mock.patch(
        "didcomm_resolver.resolver.DIDCommResolver.resolver_connections",
        mock.CoroutineMock(return_value=[]),
    ):
        with pytest.raises(DIDMethodNotSupported):
            await resolver._resolve(profile, "did:example:1234abcd")


@pytest.mark.asyncio
async def test_set_resolver_connection(profile, MockConnRecord):
    conn_id = "test"
    methods = {"example"}
    async with profile.session() as session:
        resolver_connection = await DIDCommResolver.set_resolver_connection(
            session, conn_id, methods
        )
    assert resolver_connection.connection_id == conn_id
    assert resolver_connection.methods == methods


@pytest.mark.asyncio
async def test_from_metadata_record(profile, MockConnRecord):
    mock = MagicMock()
    mock.value = '{"methods": "sovtest"}'
    result = ResolverConnection.from_metadata_record(mock)
    assert "sovtest" == result[1]


@pytest.mark.asyncio
async def test_from_connection_id_fail(profile, MockConnRecord):
    mock = MagicMock()

    async def return_none(*args):
        return None

    MockConnRecord.metadata_get.side_effect = return_none
    MockConnRecord.retrieve_by_id.return_value = MockConnRecord

    with pytest.raises(StorageNotFoundError):
        await ResolverConnection.from_connection_id(mock, mock)


@pytest.mark.asyncio
async def test_resolver_connections(profile, MockConnRecord):
    resolver_connections = []

    async def aux(*args, **kwargs):
        return resolver_connections

    session = mock.MagicMock()
    matching = mock.MagicMock()
    session.find_all_records.side_effect = aux
    session.inject.return_value = session

    result = await DIDCommResolver.resolver_connections(session, matching)
    assert resolver_connections == result
