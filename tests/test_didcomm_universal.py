"""Test universal resolver with did-comm messaging."""
import os
from unittest.mock import MagicMock, AsyncMock, patch

import pytest
from aries_cloudagent.storage.record import StorageRecord
from asynctest import mock as async_mock

from aries_cloudagent.resolver.base import ResolverError
from didcomm_uniresolver import DIDCommUniversalDIDResolver
from aries_cloudagent.messaging.request_context import RequestContext

# pylint: disable=redefined-outer-name
from tests import DOC


@pytest.fixture
def resolver():
    """Resolver fixture."""
    uni_resolver = DIDCommUniversalDIDResolver()
    uni_resolver.configure(
        {
            "endpoint": "https://dev.uniresolver.io/1.0/identifiers",
            "methods": [
                "sov",
                "abt",
                "btcr",
                "erc725",
                "dom",
                "stack",
                "ethr",
                "web",
                "v1",
                "key",
                "ipid",
                "jolo",
                "hacera",
                "elem",
                "seraphid",
                "github",
                "ccp",
                "work",
                "ont",
                "kilt",
                "evan",
                "echo",
                "factom",
                "dock",
                "trust",
                "io",
                "bba",
                "bid",
                "schema",
                "ion",
                "ace",
                "gatc",
                "unisot",
                "icon",
            ],
        }
    )
    yield uni_resolver


@pytest.fixture
def profile():
    """Profile fixture."""
    yield async_mock.MagicMock()


class MockResponse:
    """Mock didcomm response."""
    pass


class MockClientSession:
    """Mock client session."""

    def __init__(self, response: MockResponse = None):
        self.response = response

    def __call__(self):
        return self

    async def __aenter__(self):
        """For use as async context."""
        return self

    async def __aexit__(self, err_type, err_value, err_exc):
        """For use as async context."""

    def get(self, endpoint):
        """Return response."""
        return self.response


@pytest.fixture
def context():
    yield RequestContext.test_context()


FAKE_YAML0 = "endpoint: magic\rmethods: test"


@async_mock.patch("builtins.open", new_callable=async_mock.mock_open,
                  read_data=FAKE_YAML0)
@pytest.mark.asyncio
async def test_setup(mock_open, resolver, context):
    with async_mock.patch.dict(os.environ, {"UNI_RESOLVER_CONFIG": "fake_config"}):
        await resolver.setup(context)
        assert resolver._endpoint == "magic"
        assert resolver._supported_methods == "test"

@patch("os.environ")
@pytest.mark.asyncio
async def test_setup_env_error(environ_mock, resolver, context):
    environ_mock.get.return_value = "error"
    with async_mock.patch.dict(os.environ, {"UNI_RESOLVER_fake": "bad_env_config"}):
        with pytest.raises(ResolverError):
            await resolver.setup(context)


FAKE_YAML1 = "NO_endpoint: magic\rNo_methodZ: test"


@async_mock.patch("builtins.open", new_callable=async_mock.mock_open,
                  read_data=FAKE_YAML1)
@pytest.mark.asyncio
async def test_setup_yaml_error(mock_open, resolver, context):
    with async_mock.patch.dict(os.environ, {"UNI_RESOLVER_CONFIG": "fake_config"}):
        with pytest.raises(ResolverError):
            await resolver.setup(context)


def test_supported_methods(resolver):
    assert resolver.supported_methods


def test_configre_error(resolver):
    with pytest.raises(ResolverError):
        resolver.configure({"fake": "configure"})

@patch('didcomm_uniresolver.didcomm_universal.ResolveDIDResult')
async def test_resolve_dict(ResolveDIDMock, resolver, profile):
    did_example = "did:sov:201029023831"
    mock_inject = MagicMock()
    mock_inject.inject.return_value = True

    records = AsyncMock()
    records.find_all_records.return_value = [
        StorageRecord(type="connection_metadata", value="world",
                      tags={"key": "didcomm_uniresolver",
                            "connection_id": "1732d18d-c6f6-4e68-b3a7-56cc31d3313b"},
                      id="5b9b78a061e6435bbbd7d5cde02d4192")]
    profile.session.return_value.__aenter__.return_value.inject.return_value = records

    async def aux(*args, **kwargs):
        mock = MagicMock()
        mock.did_document = DOC
        return mock

    ResolveDIDMock.Handler.response_to = aux

    result = await resolver.resolve(profile, did_example)

    assert result == DOC


@patch('didcomm_uniresolver.didcomm_universal.ResolveDIDResult')
async def test_resolve_pydid(ResolveDIDMock, resolver, profile):
    did_example = "did:sov:201029023831"
    mock_inject = MagicMock()
    mock_inject.inject.return_value = True

    records = AsyncMock()
    records.find_all_records.return_value = [
        StorageRecord(type="connection_metadata", value="world",
                      tags={"key": "didcomm_uniresolver",
                            "connection_id": "1732d18d-c6f6-4e68-b3a7-56cc31d3313b"},
                      id="5b9b78a061e6435bbbd7d5cde02d4192")]
    profile.session.return_value.__aenter__.return_value.inject.return_value = records

    async def aux(*args, **kwargs):
        mock = MagicMock()
        mock.did_document.serialize.return_value = DOC
        return mock

    ResolveDIDMock.Handler.response_to = aux

    result = await resolver.resolve(profile, did_example)

    assert result == DOC


async def test_resolve_not_found(resolver, profile):
    did_example = "did:sov:201029023831"
    mock_inject = MagicMock()
    mock_inject.inject.return_value = True

    records = AsyncMock()
    records.find_all_records.return_value = []
    profile.session.return_value.__aenter__.return_value.inject.return_value = records

    with pytest.raises(ResolverError):
        await resolver.resolve(profile, did_example)
