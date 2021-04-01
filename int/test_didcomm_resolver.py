"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name

import pytest
import requests
import time
from functools import wraps

TEST_DID = "did:key:z6Mkfriq1MqLBoPWecGoDLjguo1sB9brj6wT3qZ5BxkKpuP6"
AUTO_ACCEPT = "false"

RESOLVER = "http://resolver:3001"
REQUESTER = "http://requester:3001"


def get(agent: str, path: str, **kwargs):
    """Get."""
    return requests.get(f"{agent}{path}", **kwargs)


def post(agent: str, path: str, **kwargs):
    """Post."""
    return requests.post(f"{agent}{path}", **kwargs)


def fail_if_not_ok(message: str):
    """Fail the current test if wrapped call fails with message."""

    def _fail_if_not_ok(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            if not response.ok:
                pytest.fail(f"{message}: {response.content}")
            return response

        return _wrapper

    return _fail_if_not_ok


def unwrap_json_response(func):
    """Unwrap a requests response object to json."""

    @wraps(func)
    def _wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        return response.json()

    return _wrapper


class Agent:
    """Class for interacting with Agent over Admin API"""

    def __init__(self, url: str):
        self.url = url

    @unwrap_json_response
    @fail_if_not_ok("Create invitation failed")
    def create_invitation(self, **kwargs):
        """Create invitation."""
        return post(self.url, "/connections/create-invitation", params=kwargs)

    @unwrap_json_response
    @fail_if_not_ok("Receive invitation failed")
    def receive_invite(self, invite: dict, **kwargs):
        """Receive invitation."""
        return post(
            self.url, "/connections/receive-invitation", params=kwargs, json=invite
        )

    @unwrap_json_response
    @fail_if_not_ok("Accept invitation failed")
    def accept_invite(self, connection_id: str):
        """Accept invitation."""
        return post(
            self.url,
            f"/connections/{connection_id}/accept-invitation",
        )

    @unwrap_json_response
    @fail_if_not_ok("Failed to retreive connections")
    def retrieve_connections(self, connection_id: str = None, **kwargs):
        """Retrieve connections."""
        return get(
            self.url,
            "/connections" if not connection_id else f"/connections/{connection_id}",
            params=kwargs,
        )

    @unwrap_json_response
    @fail_if_not_ok("Failed to set connection metadata")
    def metadata_set(self, connection_id, **metadata):
        """Set connection metadata."""
        return post(
            self.url,
            f"/connections/{connection_id}/metadata",
            json={"metadata": metadata},
        )


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


def test_conn_invitation(resolver):
    """Test connection invitation."""
    resp = resolver.create_invitation(auto_accept="false")
    assert resp["invitation"]
    invite = resp["invitation"]
    assert invite["serviceEndpoint"]
    assert invite["recipientKeys"]


def test_conn_receive_accept_invite(resolver, requester):
    """Test connection receive accept invite."""
    invite = resolver.create_invitation(auto_accept="false")["invitation"]
    received = requester.receive_invite(invite, auto_accept="false")
    time.sleep(1)
    resp = requester.accept_invite(received["connection_id"])
    assert resp


def test_auto_accept_conn(resolver, requester):
    """Test auto accepting connection."""
    invite = resolver.create_invitation(auto_accept="true")["invitation"]
    received = requester.receive_invite(invite, auto_accept="true")
    assert received


def test_no_resolver_connection_returns_error(established_connection):
    """Test resolution over DIDComm Connection."""
    resp = requests.get("http://requester:3001/resolver/resolve/did:example:123")
    assert not resp.ok
