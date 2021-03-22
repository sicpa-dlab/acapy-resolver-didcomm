import pytest
import requests
import time

TEST_DID = "did:key:z6Mkfriq1MqLBoPWecGoDLjguo1sB9brj6wT3qZ5BxkKpuP6"
AUTO_ACCEPT = "false"

def _resolver_invitation(auto_accept=AUTO_ACCEPT):
    r = requests.post(
        "http://resolver:3001/connections/create-invitation",
        params={"auto_accept": auto_accept}
    )
    if not r.ok:
        pytest.fail(f"connections invitation creation failed!{r.content}")
    return r


def _requester_receive_invite(invite,auto_accept=AUTO_ACCEPT):
    r = requests.post(
        "http://requester:3001/connections/receive-invitation",
        params={"auto_accept": auto_accept},
        json=invite,
    )
    if not r.ok:
        pytest.fail(f"connections invitation receive failed!{r.content}")
    return r


def _requester_accept_invite(conn_id):
    r = requests.post(
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
    yield conn_id'''


def test_conn_invitation():
    r = _resolver_invitation()
    assert r.json()["invitation"]
    invite = r.json()["invitation"]
    assert invite["serviceEndpoint"]
    assert invite["recipientKeys"]
    # Todo: check created connectiion


def test_conn_receive_accept_invite():
    r = _resolver_invitation()
    invite = r.json()["invitation"]
    r = _requester_receive_invite(invite)
    assert r.ok
    time.sleep(1)
    r = _requester_accept_invite(r.json()["connection_id"])
    assert r.ok
    # Todo: check created connectiion


#def test_pass(establish_connection):
#    r = requests.get(f"http://requester:3001/resolver/resolve/{TEST_DID}")
#    if r.ok:
#        print(r.json())
#    else:
#        pytest.fail(f"resolver resolve failed!{r.content}")
