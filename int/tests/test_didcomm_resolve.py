"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name

from . import DID_MOCK, DID_SOV, DID_MOCK_FAIL

from acapy_backchannel import Client
from acapy_backchannel.api.resolver import resolve


def test_no_resolver_connection_returns_error(requester: Client):
    """Test resolution over DIDComm Connection."""
    resp = resolve.sync_detailed(client=requester, did=DID_MOCK)
    assert resp.status_code != 200


def test_no_indy_ledger_resolver_connection_returns_error(requester: Client):
    """Test resolution over DIDComm Connection."""
    resp = resolve.sync_detailed(client=requester, did=DID_SOV)


def test_mocked_resolver_connection(resolver_connection, requester: Client):
    """Test resolution over DIDComm Connection."""
    resp = resolve.sync(client=requester, did=DID_MOCK).to_dict()
    assert resp["did_document"] == {
        "@context": "https://www.w3.org/ns/did/v1",
        "id": "did:mock:test",
    }

    resolver_metadata = resp["metadata"]
    assert resolver_metadata["resolver_type"] == "non-native"
    assert resolver_metadata["resolver"] == "DIDCommResolver"


def test_mocked_failed_resolver_connection(resolver_connection, requester: Client):
    """Test resolution over DIDComm Connection."""
    resp = resolve.sync_detailed(client=requester, did=DID_MOCK_FAIL)
    assert resp.status_code != 200
