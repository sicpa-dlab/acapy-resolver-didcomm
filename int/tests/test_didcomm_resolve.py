"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name

import pytest
import requests

from . import DID_MOCK, DID_KEY, DID_SOV, DID_MOCK_FAIL

from .conftest import Agent
from acapy_client.exceptions import ApiException
from acapy_client.models import ConnectionRegisterRequest


@pytest.fixture
def resolver_connection(established_connection, requester: Agent):
    """Fixture for a registered resolver connection with cleanup."""
    requester.didcomm_resolver.register_resolver_connection(
        established_connection, body=ConnectionRegisterRequest(methods=["mock"])
    )
    yield
    requester.didcomm_resolver.unset_resolver_connection(established_connection)


def test_no_resolver_connection_returns_error(requester: Agent):
    """Test resolution over DIDComm Connection."""
    with pytest.raises(ApiException):
        requester.resolver.resolve(DID_MOCK)


def test_no_indy_ledger_resolver_connection_returns_error(requester: Agent):
    """Test resolution over DIDComm Connection."""
    with pytest.raises(ApiException):
        requester.resolver.resolve(DID_SOV)


def test_mocked_resolver_connection(resolver_connection, requester: Agent):
    """Test resolution over DIDComm Connection."""
    resp = requester.resolver.resolve(DID_MOCK)
    assert resp == {"did_doc": {
        "@context": "https://www.w3.org/ns/did/v1",
        "id": "did:mock:test:mocked_id"}
    }


def test_mocked_resolver_connection_verbose(resolver_connection, requester: Agent):
    """Test resolution over DIDComm Connection."""

    resp = requests.get(f"http://requester:3001/resolver/resolve/{DID_MOCK}",
                        params={"verbose": True}).json()
    assert resp["did_doc"] == {
        "@context": "https://www.w3.org/ns/did/v1",
        "id": "did:mock:test:mocked_id"}

    resolver_metadata = resp["resolver_metadata"]
    assert resolver_metadata["type"] == "non-native"
    assert resolver_metadata["driverId"] == "did:mock"
    assert resolver_metadata["resolver"] == "didcomm_resolver.resolver.DIDCommResolver"


def test_mocked_failed_resolver_connection(resolver_connection, requester: Agent):
    """Test resolution over DIDComm Connection."""
    with pytest.raises(ApiException):
        resp = requester.resolver.resolve(DID_MOCK_FAIL)


def test_fail_register_method_to_not_existing_conn_id(requester: Agent):
    """Test to fail the register method over DIDComm Connection."""
    with pytest.raises(ApiException):
        requester.didcomm_resolver.register_resolver_connection(
            "does not exist", body=ConnectionRegisterRequest(methods=["mock"])
        )
