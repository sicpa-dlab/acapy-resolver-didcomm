"""AwaitableHandler Base Class"""

import asyncio
from abc import abstractmethod
from asyncio import Future
from typing import Mapping

from aries_cloudagent.messaging.agent_message import AgentMessage
from aries_cloudagent.messaging.base_handler import BaseHandler
from aries_cloudagent.messaging.request_context import RequestContext
from aries_cloudagent.messaging.responder import BaseResponder


class AwaitableHandler(BaseHandler):
    """Enable awaiting a message handled by this handler."""

    pending_futures: Mapping[str, Future] = {}

    @classmethod
    def response_to(cls, request: AgentMessage) -> Future:
        """Await the response to a message.

        The ID of the passed in message (the requesting message) is used as the
        correlator between pending future and response.
        """
        future: Future = asyncio.get_event_loop().create_future()
        cls.pending_futures[request._message_id] = future
        return future

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Execute handling of message and perform future resolution."""
        await self.do_handle(context, responder)
        if context.message._thread_id in self.pending_futures:
            future = self.pending_futures[context.message._thread_id]
            future.set_result(context.message)
            future.result()

    @abstractmethod
    async def do_handle(self, context: RequestContext, responder: BaseResponder):
        """Handle the message."""


class AwaitableErrorHandler(AwaitableHandler):
    """Raise an error from the response instead of returning a result."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Execute handle of message and perform future resolution with an error."""
        await self.do_handle(context, responder)
        if context.message._thread_id in self.pending_futures:
            future = self.pending_futures[context.message._thread_id]
            future.set_exception(self.map_exception(context.message))
            future.result()
    
    @abstractmethod
    def map_exception(self, message: AgentMessage):
        """Map a message to an exception that should be raised."""
