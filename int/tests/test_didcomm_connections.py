"""Integration tests for DIDComm resolver."""

# pylint: disable=redefined-outer-name, unused-argument

from acapy_backchannel import Client
from acapy_backchannel.api.didcomm_resolver import (
    register_resolver_connection,
    resolver_connections,
    unset_resolver_connection,
    resolver_connection as get_resolver_connection,
)
from acapy_backchannel.models.connection_register_request import (
    ConnectionRegisterRequest,
)


def test_retrieve_zero_connections(requester: Client):
    """Test retrieve DIDComm Connections."""
    resp = resolver_connections.sync(client=requester)
    assert len(resp.results) == 0


def test_register_didcomm_connection(requester: Client, resolver_connection):
    """Test retrieve DIDComm Connections."""
    resp = resolver_connections.sync(client=requester)
    assert resp.results


def test_retrieve_connections(requester: Client, resolver_connection):
    """Test retrieve DIDComm Connections."""
    resp = resolver_connections.sync(client=requester)
    assert len(resp.results) == 1


def test_retrieve_specific_connection_by_id(
    requester: Client, established_connection, resolver_connection
):
    """Test retrieve DIDComm Connections by id."""
    resp = get_resolver_connection.sync(
        client=requester, conn_id=established_connection
    )
    assert resp.connection_id == established_connection


def test_fail_to_retrieve_no_existing_specific_connection_by_id(requester: Client):
    """Test to fail the retrieve DIDComm Connections by id."""
    resp = get_resolver_connection.sync_detailed(client=requester, conn_id="DNE")
    assert resp.status_code == 400


def test_unset_resolver_connection(established_connection, requester: Client):
    """Test remove DIDComm resolver Connection record."""
    register_resolver_connection.sync(
        client=requester,
        conn_id=established_connection,
        json_body=ConnectionRegisterRequest(methods=["test"]),
    )
    unset_resolver_connection.sync(client=requester, conn_id=established_connection)
    resp = resolver_connections.sync(client=requester)
    assert len(resp.results) == 0


def test_fail_to_remove_no_existing_connection_record(requester: Client):
    """Test to fail the remove DIDComm Connection record."""
    resp = unset_resolver_connection.sync_detailed(client=requester, conn_id="DNE")
    assert resp.status_code == 404


def test_fail_register_method_to_not_existing_conn_id(requester: Client):
    """Test to fail the register method over DIDComm Connection."""
    resp = register_resolver_connection.sync_detailed(
        client=requester,
        conn_id="DNE",
        json_body=ConnectionRegisterRequest(methods=["test"]),
    )
    assert resp.status_code != 200
