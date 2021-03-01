"""Test universal resolver with did-comm messaging."""

from typing import Dict, Union

import pytest
from asynctest import mock as async_mock

from aries_cloudagent.connections.models.diddoc_v2 import DIDDoc
from aries_cloudagent.resolver.base import DIDNotFound, ResolverError
from .. import did_comm_universal as test_module
from ..did_comm_universal import DIDCommUniversalDIDResolver

# pylint: disable=redefined-outer-name


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
def mock_client_session():
    temp = test_module.aiohttp.ClientSession
    session = MockClientSession()
    test_module.aiohttp.ClientSession = session
    yield session
    test_module.aiohttp.ClientSession = temp


@pytest.mark.asyncio
async def test_resolve(profile, resolver, mock_client_session):
    pass

@pytest.mark.asyncio
async def test_resolve_not_found(profile, resolver, mock_client_session):
    pass

@pytest.mark.asyncio
async def test_resolve_unexpeceted_status(profile, resolver, mock_client_session):
    pass
