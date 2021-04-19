"""Test AwaitableHandler classes."""

from asyncio import Future

import pytest

from asynctest import mock
from didcomm_resolver.acapy_tools.awaitable_handler import (
    AwaitableHandler,
    AwaitableErrorHandler,
    send_and_wait_for_response,
)
from aries_cloudagent.messaging.request_context import RequestContext
from aries_cloudagent.messaging.responder import BaseResponder, MockResponder
from aries_cloudagent.messaging.agent_message import AgentMessage


THREAD_ID = "test"


class ExampleHandler(AwaitableHandler):
    async def do_handle(self, context: RequestContext, responder: BaseResponder):
        """Handle Example message or something."""


class ExampleErrorHandler(AwaitableErrorHandler):
    async def do_handle(self, context: RequestContext, responder: BaseResponder):
        """Handle example error."""

    def map_exception(self, message: AgentMessage):
        """Return an exception derived from message."""
        return Exception("Testing.")


@pytest.fixture
def request_message():
    message = mock.MagicMock()
    message._message_id = THREAD_ID
    yield message


@pytest.fixture
def response_message():
    message = mock.MagicMock()
    message._thread_id = THREAD_ID
    yield message


@pytest.fixture
def context():
    yield RequestContext.test_context()


@pytest.fixture
def mock_responder():
    yield MockResponder()


@pytest.mark.asyncio
async def test_can_await(context, mock_responder, request_message, response_message):
    """Test awaitable handler can be awaited."""
    context.message = response_message
    pending_message: Future = ExampleHandler.response_to(request_message)
    await ExampleHandler().handle(context, mock_responder)
    assert pending_message.done()
    assert await pending_message == response_message


@pytest.mark.asyncio
async def test_can_awaitable_error_handler(
    context, mock_responder, request_message, response_message
):
    """ Test awaitable error handler."""
    context.message = response_message
    ExampleErrorHandler.response_to(request_message)
    with pytest.raises(Exception):
        await ExampleErrorHandler().handle(context, mock_responder)


@pytest.mark.asyncio
async def test_send_and_wait_for_response():
    message = mock.MagicMock()
    response_type = mock.MagicMock()
    responder = mock.MagicMock()

    class TestHandler(ExampleHandler):
        async def response_to(self, *args, **kwargs):
            """Handle Example message or something."""
            return "message"

    response_type.Handler = TestHandler

    async def aux(*args, **kwargs):
        return None

    responder.send = aux

    await send_and_wait_for_response(message, response_type, responder)
