"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name

import pytest
import requests
import time
from functools import wraps

DID_KEY = "did:key:z6Mkfriq1MqLBoPWecGoDLjguo1sB9brj6wT3qZ5BxkKpuP6"
DID_SOV = "did:sov:WRfXPg8dantKVubE3HX8pw"

DID_DOC_SOV = {
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
            "serviceEndpoint": "https://agents.danubeclouds.com/agent/WRfXPg8dantKVubE3HX8pw",
        },
        {
            "type": "xdi",
            "serviceEndpoint": "https://xdi03-at.danubeclouds.com/cl/+!:did:sov:WRfXPg8dantKVubE3HX8pw",
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
}

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


def test_retrieve_zero_connections(established_connection):
    """Test retrieve DIDComm Connections."""

    resp = requests.get("http://requester:3001/resolver/connections")

    assert resp.ok
    assert len(resp.json()) == 0


def test_register_didcomm_connection(established_connection):
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


def test_retrieve_connections(established_connection):
    """Test retrieve DIDComm Connections."""

    resp = requests.get("http://requester:3001/resolver/connections")

    assert resp.ok
    assert len(resp.json()) == 1


def test_retrieve_specific_connection_by_id(established_connection):
    """Test retrieve DIDComm Connections by id."""

    conn_id = requests.get("http://requester:3001/resolver/connections").json()[0][
        "connection_id"
    ]

    resp = requests.get(f"http://requester:3001/resolver/connections/{conn_id}")
    assert resp.ok
    assert resp.json()["connection_id"] == conn_id


def test_fail_to_retrieve_no_existing_specific_connection_by_id(established_connection):
    """Test to fail the retrieve DIDComm Connections by id."""

    conn_id = "not-existing-id"

    resp = requests.get(f"http://requester:3001/resolver/connections/{conn_id}")
    assert not resp.ok


def test_remove_connection_record(established_connection):
    """Test remove DIDComm Connection record."""

    conn_id = requests.get(f"http://requester:3001/resolver/connections").json()[0][
        "connection_id"
    ]

    resp = requests.delete(f"http://requester:3001/resolver/connections/{conn_id}")
    assert resp.ok
    assert resp.json() == {"results": {}}

    conections = requests.get(f"http://requester:3001/resolver/connections")

    assert conections.ok
    assert len(conections.json()) == 0


def test_fail_to_remove_no_existing_connection_record(established_connection):
    """Test to fail the remove DIDComm Connection record."""

    conn_id = "no-existing-id"
    resp = requests.delete(f"http://requester:3001/resolver/connections/{conn_id}")
    assert not resp.ok


def test_no_resolver_connection_returns_error(established_connection):
    """Test resolution over DIDComm Connection."""

    resp = requests.get(f"http://requester:3001/resolver/resolve/{DID_KEY}")

    assert not resp.ok


@pytest.mark.skip(reason="Implementation not functional yet")
def test_no_resolver_connection_returns_error(established_connection):
    """Test resolution over DIDComm Connection."""

    resp = requests.get(f"http://requester:3001/resolver/resolve/{DID_SOV}")

    assert resp.ok
    assert resp.json()["did_doc"] == DID_DOC_SOV


def test_register_method(established_connection):
    """Test register method over DIDComm Connection."""

    conn_id = requests.get(f"http://requester:3001/connections").json()["results"][0][
        "connection_id"
    ]

    method = "testingmethod"
    body = {"methods": [method]}

    resp = requests.post(
        f"http://requester:3001/resolver/register/{conn_id}", json=body
    )
    assert resp.ok
    assert resp.json() == {
        "results": {"didcomm_resolver": {"methods": ["testingmethod"]}}
    }

    methods = requests.get(f"http://requester:3001/resolver/connections").json()[0][
        "methods"
    ]

    assert method in methods


def test_fail_register_method_to_not_existing_conn_id(established_connection):
    """Test to fail the register method over DIDComm Connection."""

    conn_id = "no-existing-id"

    method = "testingmethod"
    body = {"methods": [method]}

    resp = requests.post(
        f"http://requester:3001/resolver/register/{conn_id}", json=body
    )

    assert not resp.ok


def test_update_method(established_connection):
    """Test update connection methods that are resolvable over DIDComm Connection."""

    conn_id = requests.get(f"http://requester:3001/resolver/connections").json()[0][
        "connection_id"
    ]

    method = "updatedtestingmethod"
    method2 = "newmethod"
    body = {"methods": [method, method2]}

    resp = requests.post(f"http://requester:3001/resolver/update/{conn_id}", json=body)
    assert resp.ok
    assert resp.json() == {"results": "Ok"}

    methods = requests.get(f"http://requester:3001/resolver/connections").json()[0][
        "methods"
    ]

    assert [method, method2] == methods


def test_fail_to_update_method_due_not_existing_conn_id(established_connection):
    """Test to fail the update connection methods that are resolvable over DIDComm Connection."""

    conn_id = "no-existing-id"
    method = "updatedtestingmethod"
    method2 = "newmethod"
    body = {"methods": [method, method2]}

    resp = requests.post(f"http://requester:3001/resolver/update/{conn_id}", json=body)
    assert not resp.ok


@pytest.mark.skip(reason="Implementation not functional yet")
def test_json_ld_sign(established_connection):
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
                    "serviceEndpoint": "https://agents.danubeclouds.com/agent/WRfXPg8dantKVubE3HX8pw",
                },
                {
                    "type": "xdi",
                    "serviceEndpoint": "https://xdi03-at.danubeclouds.com/cl/+!:did:sov:WRfXPg8dantKVubE3HX8pw",
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
def test_json_ld_verify(established_connection):
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
                "verificationMethod": "did:key:z6MkjRagNiMu91DduvCvgEsqLZDVzrJzFrwahc4tXLt9DoHd#z6MkjRagNiMu91DduvCvgEsqLZDVzrJzFrwahc4tXLt9DoHd",
                "proofPurpose": "assertionMethod",
                "jws": "eyJhbGciOiJFZERTQSIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..l9d0YHjcFAH2H4dB9xlWFZQLUpixVCWJk0eOt4CXQe1NXKWZwmhmn9OQp6YxX0a2LffegtYESTCJEoGVXLqWAA",
            },
        },
    }

    resp = requests.post("http://requester:3001/jsonld/verify", json=body)
    assert resp.ok
    assert resp.json() == {"valid": True}
