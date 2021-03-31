import pytest
import requests
import time
from functools import wraps
import json

TEST_DID = "did:key:z6Mkfriq1MqLBoPWecGoDLjguo1sB9brj6wT3qZ5BxkKpuP6"
AUTO_ACCEPT = "false"

RESOLVER = "http://resolver:3001"
REQUESTER = "http://requester:3001"


def get(agent: str, path: str, **kwargs):
    return requests.get(f"{agent}{path}", **kwargs)


def post(agent: str, path: str, **kwargs):
    return requests.post(f"{agent}{path}", **kwargs)


def fail_if_not_ok(message: str):
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
    @wraps(func)
    def _wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        return response.json()
    return _wrapper


class Agent:
    def __init__(self, url: str):
        self.url = url

    @unwrap_json_response
    @fail_if_not_ok("Create invitation failed")
    def create_invitation(self, **kwargs):
        return post(self.url, "/connections/create-invitation", params=kwargs)

    @unwrap_json_response
    @fail_if_not_ok("Receive invitation failed")
    def receive_invite(self, invite: dict, **kwargs):
        return post(
            self.url,
            "/connections/receive-invitation",
            params=kwargs,
            json=invite
        )

    @unwrap_json_response
    @fail_if_not_ok("Accept invitation failed")
    def accept_invite(self, connection_id: str):
        return get(
            self.url,
            "/connections/accept-invitation",
            params={"conn_id": connection_id}
        )

    @unwrap_json_response
    @fail_if_not_ok("Failed to retreive connections")
    def retrieve_connections(self, connection_id: str = None, **kwargs):
        return get(
            self.url,
            "/connections" if not connection_id else f"/connections/{connection_id}",
            params=kwargs
        )


@pytest.fixture
def requester():
    yield Agent(REQUESTER)


@pytest.fixture
def resolver():
    yield Agent(RESOLVER)


def _requester_accept_invite(conn_id):
    r = requests.get(
        "http://requester:3001/connections/accept-invitation",
        params={"conn_id": conn_id}
    )
    if not r.ok:
        pytest.fail(f"connections invitation accept failed!{r.content}")
    return r


'''@pytest.fixture(scope="session", autouse=True)
def establish_connection():
    invite = _resolver_invitation(auto_accept="true").json()["invitation"]
    r = _requester_receive_invite(invite,auto_accept="true")
    conn_id = r.json()["connection_id"]
    time.sleep(3)
    yield conn_id '''


def test_conn_invitation(resolver):
    resp = resolver.create_invitation(auto_accept="false")
    assert resp["invitation"]
    invite = resp["invitation"]
    assert invite["serviceEndpoint"]
    assert invite["recipientKeys"]
    # Todo: check created connectiion


def test_conn_receive_accept_invite(resolver, requester):
    invite = resolver.create_invitation(auto_accept="false")["invitation"]
    #print(json.dumps(resolver.retrieve_connections(), indent=2))
    received = requester.receive_invite(invite,auto_accept="false")
    #print(json.dumps(received, indent=2))
    #print(json.dumps(requester.retrieve_connections(), indent=2))
    time.sleep(1)
    resp = requester.accept_invite(received["connection_id"])
    # Todo: check created connectiion


def test_auto_accept_conn(resolver, requester):
    invite = resolver.create_invitation(auto_accept="true")["invitation"]
    received = requester.receive_invite(invite,auto_accept="true")
    print(received)
    # Todo: check created connectiion


#def test_pass(establish_connection):
#    r = requests.get(f"http://requester:3001/resolver/resolve/{TEST_DID}")
#    if r.ok:
#        print(r.json())
#    else:
#        pytest.fail(f"resolver resolve failed!{r.content}")
