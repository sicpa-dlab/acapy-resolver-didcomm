"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name

import time

import pytest
import requests
from . import Agent, REQUESTER, RESOLVER


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


def test_retrieve_zero_connections():
    """Test retrieve DIDComm Connections."""

    resp = requests.get("http://requester:3001/resolver/connections")

    assert resp.ok
    assert len(resp.json()) == 0


def test_register_didcomm_connection():
    """Test retrieve DIDComm Connections."""

    body = {
        "metadata": {"didcomm_resolver": {"methods": ["test"]}},
        "recipient_keys": ["H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"],
        "routing_keys": ["H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"],
        "service_endpoint": "http://requester:3001",
    }

    resp = requests.post(
        "http://requester:3001/connections/create-invitation", json=body
    )

    assert resp.ok


def test_retrieve_connections():
    """Test retrieve DIDComm Connections."""

    resp = requests.get("http://requester:3001/resolver/connections")

    assert resp.ok
    assert len(resp.json()) == 1


def test_retrieve_specific_connection_by_id():
    """Test retrieve DIDComm Connections by id."""

    conn_id = requests.get("http://requester:3001/resolver/connections").json()[0][
        "connection_id"
    ]

    resp = requests.get(f"http://requester:3001/resolver/connections/{conn_id}")
    assert resp.ok
    assert resp.json()["connection_id"] == conn_id


def test_fail_to_retrieve_no_existing_specific_connection_by_id():
    """Test to fail the retrieve DIDComm Connections by id."""

    conn_id = "not-existing-id"

    resp = requests.get(f"http://requester:3001/resolver/connections/{conn_id}")
    assert not resp.ok


def test_remove_connection_record():
    """Test remove DIDComm Connection record."""

    conn_id = requests.get("http://requester:3001/resolver/connections").json()[0][
        "connection_id"
    ]

    resp = requests.delete(f"http://requester:3001/resolver/connections/{conn_id}")
    assert resp.ok
    assert resp.json() == {"results": {}}

    conections = requests.get("http://requester:3001/resolver/connections")

    assert conections.ok
    assert len(conections.json()) == 0


def test_fail_to_remove_no_existing_connection_record():
    """Test to fail the remove DIDComm Connection record."""

    conn_id = "no-existing-id"
    resp = requests.delete(f"http://requester:3001/resolver/connections/{conn_id}")
    assert not resp.ok
