"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name, unused-argument

from acapy_client.exceptions import ApiException
from acapy_client.models import ConnectionRegisterRequest, ReceiveInvitationRequest
import pytest

from .conftest import Agent


@pytest.fixture
def resolver_connection(established_connection, requester: Agent):
    """Fixture for a registered resolver connection with cleanup."""
    requester.didcomm_resolver.register_resolver_connection(
        established_connection, body=ConnectionRegisterRequest(methods=["test"])
    )
    yield
    requester.didcomm_resolver.unset_resolver_connection(established_connection)


def test_retrieve_zero_connections(requester: Agent):
    """Test retrieve DIDComm Connections."""
    resp = requester.didcomm_resolver.resolver_connections()
    assert len(resp["results"]) == 0


def test_register_didcomm_connection(requester: Agent, resolver_connection):
    """Test retrieve DIDComm Connections."""
    assert requester.didcomm_resolver.resolver_connections()["results"]


def test_retrieve_connections(requester: Agent, resolver_connection):
    """Test retrieve DIDComm Connections."""
    resp = requester.didcomm_resolver.resolver_connections()
    assert len(resp["results"]) == 1


def test_retrieve_specific_connection_by_id(
    requester: Agent, established_connection, resolver_connection
):
    """Test retrieve DIDComm Connections by id."""
    conn = requester.didcomm_resolver.resolver_connection(established_connection)
    assert conn["connection_id"] == established_connection


def test_fail_to_retrieve_no_existing_specific_connection_by_id(requester: Agent):
    """Test to fail the retrieve DIDComm Connections by id."""
    with pytest.raises(ApiException) as error:
        requester.didcomm_resolver.resolver_connection("doesn't exist")
        assert error.value.status == 400


def test_unset_resolver_connection(established_connection, requester: Agent):
    """Test remove DIDComm resolver Connection record."""

    requester.didcomm_resolver.register_resolver_connection(
        established_connection, body=ConnectionRegisterRequest(methods=["test"])
    )
    requester.didcomm_resolver.unset_resolver_connection(established_connection)
    connections = requester.didcomm_resolver.resolver_connections()
    assert len(connections["results"]) == 0


def test_fail_to_remove_no_existing_connection_record(requester: Agent):
    """Test to fail the remove DIDComm Connection record."""
    with pytest.raises(ApiException) as error:
        requester.didcomm_resolver.unset_resolver_connection("doesn't exist")
        assert error.value.status == 400
