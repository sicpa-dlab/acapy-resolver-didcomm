"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name

from functools import wraps
import time

import pytest
import requests

from . import Agent, REQUESTER, RESOLVER, DID_MOCK, DID_KEY, DID_SOV, DID_MOCK_FAIL

@pytest.fixture(scope="session")
def requester():
    """requester agent fixture."""
    yield Agent(REQUESTER)


@pytest.fixture(scope="session")
def resolver():
    """resolver agent fixture."""
    yield Agent(RESOLVER)


@pytest.fixture(scope="session", autouse=True)
def established_connection(resolver, requester):
    """Established connection filter."""
    invite = resolver.create_invitation(auto_accept="true")["invitation"]
    resp = requester.receive_invite(invite, auto_accept="true")
    yield resp["connection_id"]

def test_mocked_resolver_connection(established_connection, requester: Agent):
    """Test resolution over DIDComm Connection."""
    requester.post(
        f"/resolver/register/{established_connection}",
        fail_with="Failed to register connection as resolver for mock method",
        json={"methods": ["mock"]},
    )
    resp = requester.get(
        f"/resolver/resolve/{DID_MOCK}", fail_with=f"Failed to resolve DID {DID_MOCK}"
    )
    assert resp == {
        "@context": "https://www.w3.org/ns/did/v1",
        "id": "did:mock:test:mocked_id",
    }