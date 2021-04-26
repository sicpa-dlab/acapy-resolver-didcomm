"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name

import pytest
import requests

from . import Agent, REQUESTER, RESOLVER

from .jsonld_examples import JSONLD_LIST, JSONLD_FAIL_TO_RESOLVE


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


@pytest.mark.skip(reason="Implementation not functional yet")
def test_json_ld_sign():
    """Test sign json ld."""
    # TODO: Implement when route is available

    body = {
        "document": {
            "@context": ["https://www.w3.org/ns/did/v1"],
            "id": "did:sov:WRfXPg8dantKVubE3HX8pw",
            "verificationMethod": [
                {
                    "type": "Ed25519VerificationKey2018",
                    "id": "did:sov:WRfXPg8dantKVubE3HX8pw#key-1",
                    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV",
                }
            ],
            "service": [
                {
                    "type": "agent",
                    "serviceEndpoint": "https://agents.danubeclouds.com/agent/"
                    "WRfXPg8dantKVubE3HX8pw",
                },
                {
                    "type": "xdi",
                    "serviceEndpoint": "https://xdi03-at.danubeclouds.com/cl/+!"
                    ":did:sov:WRfXPg8dantKVubE3HX8pw",
                },
            ],
            "authentication": [
                {
                    "type": "Ed25519VerificationKey2018",
                    "id": "did:sov:WRfXPg8dantKVubE3HX8pw#key-1",
                    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV",
                }
            ],
            "assertionMethod": [
                {
                    "type": "Ed25519VerificationKey2018",
                    "id": "did:sov:WRfXPg8dantKVubE3HX8pw#key-1",
                    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV",
                }
            ],
        },
        "verificationMethod": "did:sov:WRfXPg8dantKVubE3HX8pw#key-1",
    }

    resp = requests.post("http://requester:3001/jsonld/sign", json=body)

    assert resp.ok


@pytest.mark.skip(reason="Implementation not functional yet")
@pytest.mark.parametrize("jsonld", JSONLD_LIST)
def test_json_ld_verify(jsonld):
    """ Verify sign for json ld"""
    # TODO: Implement when route is available
    body = {"doc": jsonld}

    resp = requests.post("http://requester:3001/jsonld/verify", json=body)
    assert resp.ok
    assert resp.json() == {"valid": True}


@pytest.mark.skip(reason="Implementation not functional yet")
def test_fail_json_ld_verify_due_resolver():
    """ Verify sign for json ld"""
    # TODO: Implement when route is available
    body = {"doc": JSONLD_FAIL_TO_RESOLVE}

    resp = requests.post("http://requester:3001/jsonld/verify", json=body)
    assert not resp.ok



