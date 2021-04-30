"""AwaitableHandler Base Class"""

import asyncio
from abc import abstractmethod
from asyncio import Future
from typing import MutableMapping, Optional, Type
from aries_cloudagent.core.error import BaseError

from aries_cloudagent.messaging.agent_message import AgentMessage
from aries_cloudagent.messaging.base_handler import BaseHandler
from aries_cloudagent.messaging.request_context import RequestContext
from aries_cloudagent.messaging.responder import BaseResponder


class WaitingForMessageFailed(BaseError):
    """Raised when failed to wait for a message."""


async def send_and_wait_for_response(
    message: AgentMessage,
    response_type: Type[AgentMessage],
    responder: BaseResponder,
    timeout: Optional[int] = None,
    **send_kwargs
):
    """Send a message and await a message of type."""
    assert issubclass(response_type.Handler, AwaitableHandler)
    response_handle: Future = response_type.Handler.response_to(message)
    await responder.send(message, **send_kwargs)
    try:
        return await asyncio.wait_for(response_handle, timeout=timeout)
    except asyncio.TimeoutError:
        response_type.Handler.cleanup_future(request=message)
        raise WaitingForMessageFailed("No response received in time")


class AwaitableHandler(BaseHandler):
    """Enable awaiting a message handled by this handler."""

    pending_futures: MutableMapping[str, Future] = {}

    @classmethod
    def response_to(cls, request: AgentMessage) -> Future:
        """Await the response to a message.

        The ID of the passed in message (the requesting message) is used as the
        correlator between pending future and response.
        """
        future: Future = asyncio.get_event_loop().create_future()
        cls.pending_futures[request._message_id] = future
        return future

    @classmethod
    def resolve_future(cls, response: AgentMessage):
        """Resolve a pending future with the passed response."""
        if response._thread_id in cls.pending_futures:
            future = cls.pending_futures[response._thread_id]
            future.set_result(response)
            future.result()
            cls.cleanup_future(response=response)

    @classmethod
    def exception_on_future(cls, response: AgentMessage, exception: Exception):
        """Resolve a pending future with an exception."""
        if response._thread_id in cls.pending_futures:
            future = cls.pending_futures[response._thread_id]
            future.set_exception(exception)
            future.result()
            cls.cleanup_future(response=response)

    @classmethod
    def cleanup_future(
        cls, request: AgentMessage = None, response: AgentMessage = None
    ):
        if request:
            key = request._message_id
        elif response:
            key = response._thread_id
        else:
            raise ValueError("Either a request or a response must be given")

        del cls.pending_futures[key]

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Execute handling of message and perform future resolution."""
        await self.do_handle(context, responder)
        self.resolve_future(context.message)

    @abstractmethod
    async def do_handle(self, context: RequestContext, responder: BaseResponder):
        """Handle the message."""


class AwaitableErrorHandler(AwaitableHandler):
    """Raise an error from the response instead of returning a result."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Execute handle of message and perform future resolution with an error."""
        await self.do_handle(context, responder)
        self.exception_on_future(context.message, self.map_exception(context.message))

    @abstractmethod
    def map_exception(self, message: AgentMessage) -> Exception:
        """Map a message to an exception that should be raised."""
