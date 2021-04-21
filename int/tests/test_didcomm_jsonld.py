"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name

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
def test_json_ld_verify():
    """ Verify sign for json ld"""
    # TODO: Implement when route is available

    body = {
        "verkey": "5yKdnU7ToTjAoRNDzfuzVTfWBH38qyhE1b9xh4v8JaWF",
        "doc": {
            "@context": [
                "https://www.w3.org/2018/credentials/v1",
                "https://www.w3.org/2018/credentials/examples/v1",
            ],
            "id": "http://example.gov/credentials/3732",
            "type": ["VerifiableCredential", "UniversityDegreeCredential"],
            "issuer": "did:key:z6MkjRagNiMu91DduvCvgEsqLZDVzrJzFrwahc4tXLt9DoHd",
            "issuanceDate": "2020-03-10T04:24:12.164Z",
            "credentialSubject": {
                "id": "did:key:z6MkjRagNiMu91DduvCvgEsqLZDVzrJzFrwahc4tXLt9DoHd",
                "degree": {
                    "type": "BachelorDegree",
                    "name": "Bachelor of Science and Arts",
                },
            },
            "proof": {
                "type": "Ed25519Signature2018",
                "created": "2020-04-10T21:35:35Z",
                "verificationMethod": "did:key:z6MkjRagNiMu91DduvCvgEsqLZDVzrJz"
                "Frwahc4tXLt9DoHd#z6MkjRagNiMu91DduvCvgEsqLZDVzrJzFrwahc4tXLt9DoHd",
                "proofPurpose": "assertionMethod",
                "jws": "eyJhbGciOiJFZERTQSIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19.."
                "l9d0YHjcFAH2H4dB9xlWFZQLUpixVCWJk0eOt4CXQe1NXKWZwmhmn9OQp6YxX0"
                "a2LffegtYESTCJEoGVXLqWAA",
            },
        },
    }

    resp = requests.post("http://requester:3001/jsonld/verify", json=body)
    assert resp.ok
    assert resp.json() == {"valid": True}
