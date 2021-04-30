"""Common fixtures."""

import os
import time
import pytest

from acapy_client import ApiClient, Configuration
from acapy_client.apis import ConnectionApi, DidcommResolverApi, ResolverApi
from acapy_client.models import ReceiveInvitationRequest


class Agent:
    def __init__(self, config: Configuration):
        self.config = config
        self.client = ApiClient(config)
        self.didcomm_resolver = DidcommResolverApi(self.client)
        self.connections = ConnectionApi(self.client)
        self.resolver = ResolverApi(self.client)


@pytest.fixture(scope="session")
def requester():
    url = os.environ.get("REQUESTER", "http://requester:3001")
    yield Agent(Configuration(host=url))


@pytest.fixture(scope="session")
def resolver():
    url = os.environ.get("RESOLVER", "http://resolver:3001")
    yield Agent(Configuration(host=url))


@pytest.fixture(scope="session", autouse=True)
def established_connection(resolver, requester):
    """Established connection filter."""
    invite = resolver.connections.create_invitation(auto_accept="true").invitation
    resp = requester.connections.receive_invitation(
        body=ReceiveInvitationRequest(**invite.to_dict()), auto_accept="true"
    )
    time.sleep(1)
    yield resp["connection_id"]
