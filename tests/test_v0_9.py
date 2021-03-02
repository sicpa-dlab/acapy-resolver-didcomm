"""Test Protocol handlers of DID Resolution protocl v0.9."""

import pytest

from asynctest import mock
from didcomm_uniresolver.v0_9 import ResolveDID, ResolveDIDResult
from aries_cloudagent.messaging.request_context import RequestContext
from aries_cloudagent.messaging.responder import MockResponder


@pytest.fixture
def responder():
    yield MockResponder()


@pytest.fixture
def message():
    yield ResolveDID(did="did:example:123abc")


@pytest.fixture
def context(message):
    con = RequestContext.test_context()
    con.message = message
    con.update_settings(
        {"didcomm_uniresolver.endpoint": "http://example.com"}
    )
    yield con


@pytest.fixture
def mock_resolve_did():
    with mock.patch.object(
        ResolveDID,
        "resolve_did",
        mock.CoroutineMock(return_value={"id": "did:example:123"})
    ) as resolve_did:
        yield resolve_did


@pytest.mark.asyncio
async def test_handle_resolve_did(context, responder, message, mock_resolve_did):
    """Test resolve did handler."""
    await message.handle(context, responder)
    assert len(responder.messages) == 1
    (result, _), *_ = responder.messages
    assert isinstance(result, ResolveDIDResult)
    assert result.did_document == {"id": "did:example:123"}
