"""Common fixtures."""

import os
import time

from acapy_backchannel import Client
from acapy_backchannel.api.connection import create_invitation, receive_invitation
from acapy_backchannel.api.didcomm_resolver import (
    register_resolver_connection,
    unset_resolver_connection,
)
from acapy_backchannel.models.connection_register_request import (
    ConnectionRegisterRequest,
)
from acapy_backchannel.models.create_invitation_request import CreateInvitationRequest
from acapy_backchannel.models.receive_invitation_request import ReceiveInvitationRequest
import pytest


@pytest.fixture(scope="session")
def requester():
    url = os.environ.get("REQUESTER", "http://requester:3001")
    yield Client(base_url=url)


@pytest.fixture(scope="session")
def resolver():
    url = os.environ.get("RESOLVER", "http://resolver:3001")
    yield Client(base_url=url)


@pytest.fixture(scope="session", autouse=True)
def established_connection(resolver: Client, requester: Client):
    """Establish connection fixture."""
    invite = create_invitation.sync(
        json_body=CreateInvitationRequest(), client=resolver, auto_accept="true"
    ).invitation
    resp = receive_invitation.sync(
        client=requester,
        auto_accept="true",
        json_body=ReceiveInvitationRequest.from_dict(invite.to_dict()),
    )
    time.sleep(1)
    yield resp.connection_id


@pytest.fixture
def resolver_connection(established_connection, requester: Client):
    """Fixture for a registered resolver connection with cleanup."""
    register_resolver_connection.sync(
        client=requester,
        conn_id=established_connection,
        json_body=ConnectionRegisterRequest(methods=["mock"]),
    )
    yield
    unset_resolver_connection.sync(client=requester, conn_id=established_connection)
