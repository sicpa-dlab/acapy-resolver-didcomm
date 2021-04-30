# pylint: disable=redefined-outer-name

from functools import wraps
import time

import pytest
import requests

DID_KEY = "did:key:z6Mkfriq1MqLBoPWecGoDLjguo1sB9brj6wT3qZ5BxkKpuP6"
DID_SOV = "did:sov:WRfXPg8dantKVubE3HX8pw"
DID_MOCK = "did:mock:test"
DID_MOCK_FAIL = "did:mock:fail"

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
            "serviceEndpoint": "https://agents.danubeclouds.com/agent/"
            "WRfXPg8dantKVubE3HX8pw",
        },
        {
            "type": "xdi",
            "serviceEndpoint": "https://xdi03-at.danubeclouds.com/cl/+!:"
            "did:sov:WRfXPg8dantKVubE3HX8pw",
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
    def _wrapper(*args, **kwargs) -> dict:
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

    def get(self, path: str, return_json: bool = True, fail_with: str = None, **kwargs):
        """Do get to agent endpoint."""
        wrapped_get = get
        if fail_with:
            wrapped_get = fail_if_not_ok(fail_with)(wrapped_get)
        if return_json:
            wrapped_get = unwrap_json_response(wrapped_get)

        return wrapped_get(self.url, path, **kwargs)

    def post(
        self, path: str, return_json: bool = True, fail_with: str = None, **kwargs
    ):
        """Do get to agent endpoint."""
        wrapped_post = post
        if fail_with:
            wrapped_post = fail_if_not_ok(fail_with)(wrapped_post)
        if return_json:
            wrapped_post = unwrap_json_response(wrapped_post)

        return wrapped_post(self.url, path, **kwargs)
