"""Test Protocol handlers of DID Resolution protocl v0.9."""
from unittest.mock import MagicMock

import pytest
from aries_cloudagent.messaging.base_handler import HandlerException
from aries_cloudagent.messaging.request_context import RequestContext
from aries_cloudagent.messaging.responder import MockResponder
from asynctest import mock

from didcomm_resolver.protocol.v0_9 import (
    ResolveDID,
    ResolveDIDResult,
    ResolveDIDProblemReport,
)

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
    result = MagicMock()
    result.did_document = {"id": "did:example:123"}
    result.resolver_metadata
    with mock.patch.object(
            ResolveDID,
            "resolve_did",
            mock.CoroutineMock(return_value=result),
    ) as resolve_did:
        yield resolve_did


@pytest.mark.asyncio
async def test_resolve_did(message):
    mock_metadata = {
            "resolver_type": "non-native",
            "resolver": "MockResolver",
            "retrieved_time": "2021-05-19T11:37:00Z",
            "duration": 41
        }

    async def aux(*args, **kwargs):
        result = MagicMock()
        result.did_document = DOC
        result.metadata = mock_metadata
        return result

    context = mock.MagicMock()
    context.resolve_with_metadata.side_effect = aux
    context.inject.return_value = context

    resolution = await message.resolve_did(context, "did:example:1234abcd")

    assert resolution.did_document == DOC
    assert resolution.metadata == mock_metadata


@pytest.mark.asyncio
async def test_resolve_did_response(resolved_did):
    assert isinstance(resolved_did, ResolveDIDResult)


@pytest.mark.asyncio
async def test_handler_do_handle(resolved_did, context, responder):
    handler = resolved_did.Handler()
    assert handler.do_handle(context, responder)
    # TODO: actually test something


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.protocol.v0_9.ResolveDIDProblemReport")
@mock.patch("didcomm_resolver.protocol.v0_9.ResolveDID.resolve_did")
async def test_resolve_did_error(resolve_did, problem, context, responder, message):
    async def raise_exc(*args, **kwargs):
        raise Exception("test_exc")

    resolve_did.side_effect = raise_exc

    with pytest.raises(HandlerException):
        await message.handle(context, responder)


@pytest.mark.asyncio
async def test_handle_resolve_did(context, responder, message, mock_resolve_did):
    """Test resolve did handler."""
    await message.handle(context, responder)
    assert len(responder.messages) == 1
    (result, _), *_ = responder.messages
    assert isinstance(result, ResolveDIDResult)
    assert result.did_document == {"id": "did:example:123"}


@pytest.mark.asyncio
async def test_handle_resolve_did_fail(context, responder, message, mock_resolve_did):
    """Test resolve did handler."""
    context.message = "error"
    with pytest.raises(HandlerException):
        await message.handle(context, responder)


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.protocol.v0_9.ResolveDIDProblemReport")
async def test_handle_error(context, responder, message, mock_resolve_did):
    """Test resolve did handler."""
    mock_resolve_did.resolve_did = mock.CoroutineMock(side_effect=HandlerException())
    with pytest.raises(HandlerException), mock.patch.object(
            ResolveDID, "resolve_did", mock.CoroutineMock(side_effect=HandlerException())
    ):
        await message.handle(context, responder)


@pytest.mark.asyncio
async def test_ResolveDIDResult_handle(resolved_did):
    context = MagicMock()
    context.message = resolved_did

    async def aux(*args, **kwargs):
        return None

    responder = MagicMock()
    responder.send_webhook.side_effect = aux
    await resolved_did.Handler().do_handle(context, responder)


@pytest.mark.asyncio
async def test_ResolveDIDResult_handle_fail(resolved_did):
    context = MagicMock()
    context.message = "Error"

    async def aux(*args, **kwargs):
        return None

    responder = MagicMock()
    responder.send_webhook.side_effect = aux
    with pytest.raises(HandlerException):
        await resolved_did.Handler().do_handle(context, responder)


@pytest.mark.asyncio
@mock.patch("didcomm_resolver.protocol.v0_9.ResolveDIDProblemReport")
async def test_ResolveDIDProblemReport_handle(resolve_did_problem):
    context = MagicMock()
    context.explain_ltxt = "mocked"
    resolved_did = ResolveDIDProblemReport()
    context.message = resolve_did_problem

    async def aux(*args, **kwargs):
        return None

    responder = MagicMock()
    responder.send_webhook.side_effect = aux

    await resolved_did.Handler().do_handle(context, responder)

    result = resolved_did.Handler().map_exception(context)
    assert "mocked" in result.message
