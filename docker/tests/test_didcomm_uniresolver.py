import pytest
import requests
import time

TEST_DID = "did:key:z6Mkfriq1MqLBoPWecGoDLjguo1sB9brj6wT3qZ5BxkKpuP6"


@pytest.fixture(scope="session", autouse=True)
def establish_connection():
    r = requests.post(
        "http://resolver:3001/connections/create-invitation",
        params={"auto_accept": "true", "multi_use": "true"},
    )
    if not r.ok:
        pytest.fail(f"connections invitation creation failed!{r.content}")
    invite = r.json()["invitation"]
    r2 = requests.post(
        "http://requester:3001/connections/receive-invitation?auto_accept=true",
        json=invite,
    )
    if not r2.ok:
        pytest.fail(f"connections invitation creation failed!{r2.content}")
    conn_id = r2.json()["connection_id"]
    time.sleep(3)
    yield conn_id


def test_pass(establish_connection):
    r = requests.get(f"http://requester:3001/resolver/resolve/{TEST_DID}")
    if r.ok:
        print(r.json())
    else:
        pytest.fail(f"resolver resolve failed!{r.content}")
