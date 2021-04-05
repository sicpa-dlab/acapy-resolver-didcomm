"""Test Protocol handlers of DID Resolution protocl v0.9."""

import pytest
from aries_cloudagent.messaging.base_handler import HandlerException
from aries_cloudagent.messaging.request_context import RequestContext
from aries_cloudagent.messaging.responder import MockResponder
from asynctest import mock

from didcomm_resolver.protocol.v0_9 import ResolveDID, ResolveDIDResult

from . import DOC


@pytest.fixture
def responder():
    yield MockResponder()


# TODO: diagnose acapy lack of support for 'locales' array in ~l10n.
@pytest.fixture
def message():
    yield ResolveDID(did="did:example:123abc", localization={"locale": "en"})


@pytest.fixture
def resolved_did():
    yield ResolveDIDResult(did_document=DOC, localization={"locale": "en"})


@pytest.fixture
def context(message):
    con = RequestContext.test_context()
    con.message = message
    con.update_settings({"didcomm_resolver.endpoint": "http://example.com"})
    yield con


@pytest.fixture
def mock_resolve_did():
    with mock.patch.object(
        ResolveDID,
        "resolve_did",
        mock.CoroutineMock(return_value={"id": "did:example:123"}),
    ) as resolve_did:
        yield resolve_did


@mock.patch("aiohttp.ClientSession.get")
@pytest.mark.asyncio
async def test_resolve_did(mock_get, message):
    mock_get.return_value.__aenter__.return_value.status = 200
    mock_get.return_value.__aenter__.return_value.json = mock.CoroutineMock(
        return_value={"didDocument": DOC}
    )
    doc = await message.resolve_did(
        "did:example:1234abcd", "https://dev.uniresolver.io/1.0/identifiers/{did}"
    )
    assert doc == DOC


@pytest.mark.asyncio
async def test_resolve_did_response(resolved_did):
    assert isinstance(resolved_did, ResolveDIDResult)


@pytest.mark.asyncio
async def test_handler_do_handle(resolved_did, context, responder):
    handler = resolved_did.Handler()
    assert handler.do_handle(context, responder)
    # TODO: actually test something


@mock.patch("aiohttp.ClientSession.get")
@pytest.mark.asyncio
async def test_resolve_did_error(mock_get, message):
    mock_get.return_value.__aenter__.return_value.status = 400
    with pytest.raises(HandlerException):
        await message.resolve_did(
            "did:example:1234abcd", "https://dev.uniresolver.io/1.0/identifiers/{did}"
        )


@pytest.mark.asyncio
async def test_handle_resolve_did(context, responder, message, mock_resolve_did):
    """Test resolve did handler."""
    await message.handle(context, responder)
    assert len(responder.messages) == 1
    (result, _), *_ = responder.messages
    assert isinstance(result, ResolveDIDResult)
    assert result.did_document == {"id": "did:example:123"}


@pytest.mark.asyncio
async def test_handle_error(context, responder, message, mock_resolve_did):
    """Test resolve did handler."""
    mock_resolve_did.resolve_did = mock.CoroutineMock(side_effect=HandlerException())
    with pytest.raises(HandlerException), mock.patch.object(
        ResolveDID, "resolve_did", mock.CoroutineMock(side_effect=HandlerException())
    ):
        await message.handle(context, responder)
