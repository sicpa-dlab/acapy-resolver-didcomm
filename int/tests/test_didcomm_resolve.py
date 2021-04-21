"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name

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


def test_no_resolver_connection_returns_error():
    """Test resolution over DIDComm Connection."""

    resp = requests.get(f"http://requester:3001/resolver/resolve/{DID_KEY}")

    assert not resp.ok


def test_no_indy_ledger_resolver_connection_returns_error():
    """Test resolution over DIDComm Connection."""

    resp = requests.get(f"http://requester:3001/resolver/resolve/{DID_SOV}")
    assert not resp.ok
    assert resp.status_code == 500


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


def test_mocked_failed_resolver_connection(requester: Agent):
    """Test resolution over DIDComm Connection."""

    resp = requester.get(
        f"/resolver/resolve/{DID_MOCK_FAIL}",
        return_json=False,
    )
    assert not resp.ok
    assert resp.status_code == 404


def test_register_method(established_connection):
    """Test register method over DIDComm Connection."""

    method = "testingmethod"
    body = {"methods": [method]}

    resp = requests.post(
        f"http://requester:3001/resolver/register/{established_connection}", json=body
    )
    assert resp.ok
    assert resp.json() == {
        "results": {"didcomm_resolver": {"methods": ["testingmethod"]}}
    }

    methods = requests.get("http://requester:3001/resolver/connections").json()[0][
        "methods"
    ]

    assert method in methods


def test_fail_register_method_to_not_existing_conn_id():
    """Test to fail the register method over DIDComm Connection."""

    conn_id = "no-existing-id"

    method = "testingmethod"
    body = {"methods": [method]}

    resp = requests.post(
        f"http://requester:3001/resolver/register/{conn_id}", json=body
    )

    assert not resp.ok


def test_update_method():
    """Test update connection methods that are resolvable over DIDComm Connection."""

    conn_id = requests.get("http://requester:3001/resolver/connections").json()[0][
        "connection_id"
    ]

    method = "updatedtestingmethod"
    method2 = "newmethod"
    body = {"methods": [method, method2]}

    resp = requests.post(f"http://requester:3001/resolver/update/{conn_id}", json=body)
    assert resp.ok
    assert resp.json() == {"results": "Ok"}

    methods = requests.get("http://requester:3001/resolver/connections").json()[0][
        "methods"
    ]

    assert [method, method2] == methods


def test_fail_to_update_method_due_not_existing_conn_id():
    """
    Test to fail the update connection methods that are resolvable over
    DIDComm Connection.
    """

    conn_id = "no-existing-id"
    method = "updatedtestingmethod"
    method2 = "newmethod"
    body = {"methods": [method, method2]}

    resp = requests.post(f"http://requester:3001/resolver/update/{conn_id}", json=body)
    assert not resp.ok


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
