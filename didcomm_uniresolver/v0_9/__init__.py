"""DID Resolution Protocol v0.9 message and handler definitions."""

import json
from datetime import datetime
from typing import Union

from aries_cloudagent.messaging.base_handler import (
    BaseHandler, BaseResponder, HandlerException, RequestContext
)
from marshmallow import fields

from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from aries_cloudagent.messaging.util import datetime_now, datetime_to_str
from aries_cloudagent.messaging.valid import INDY_ISO8601_DATETIME

from aries_cloudagent.protocols.didcomm_prefix import DIDCommPrefix

SPEC_URI = (
    "https://github.com/hyperledger/aries-rfcs/tree/"
    "6509b84abaf5760a8ba1744c8078d513f28456db/features/"
    "0124-did-resolution-protocol"
)

PROTOCOL_URI = "https://didcomm.org/did_resolution/0.1"

RESOLVE = f"{PROTOCOL_URI}/resolve"
RESOLVE_RESULT = f"{PROTOCOL_URI}/resolve_result"

PROTOCOL_PACKAGE = "aries_cloudagent.protocols.resolve_did.v0_9"

MESSAGE_TYPES = DIDCommPrefix.qualify_all(
    {
        RESOLVE: f"{PROTOCOL_PACKAGE}.messages.resolve_did.ResolveDid",
        RESOLVE_RESULT: f"{PROTOCOL_PACKAGE}.messages.resolve_did_result.ResolveDidResult"
    }
)

class ResolveDid(AgentMessage):
    """Class defining the structure of a resolve did message."""

    class Meta:
        """Basic message metadata class."""

        handler_class = HANDLER_CLASS
        message_type = RESOLVE
        schema_class = "ResolveDidSchema"

    def __init__(
        self,
        *,
        sent_time: Union[str, datetime] = None,
        did: str = None,
        localization: str = None,
        **kwargs,
    ):
        """
        TODO: update doc
        Initialize basic message object.
        Args:
            sent_time: Time message was sent
            did: did to resolve
            localization: localization
        """
        super().__init__(**kwargs)
        if not sent_time:
            sent_time = datetime_now()
        if localization:
            self._decorators["l10n"] = localization
        self.sent_time = datetime_to_str(sent_time)
        self.did = did


class ResolveDidSchema(AgentMessageSchema):
    """Basic message schema class."""

    class Meta:
        """Resolve DID message schema metadata."""

        model_class = ResolveDid

    sent_time = fields.Str(
        required=False,
        description="Time message was sent, ISO8601 with space date/time separator",
        **INDY_ISO8601_DATETIME,
    )
    did = fields.Str(required=True, description="DID",
                     example="did:sov:WRfXPg8dantKVubE3HX8pw",)


# TODO: add further response fields/options, see
# https://github.com/hyperledger/aries-rfcs/tree/master/features/0124-did-resolution-protocol#resolve-message

HANDLER_CLASS = \
    f"{PROTOCOL_PACKAGE}.handlers.resolve_did_result_handler.ResolveDidResultHandler"


class ResolveDidResult(AgentMessage):
    """Class defining the structure of a resolve did message."""

    class Meta:
        """Basic message metadata class."""

        handler_class = HANDLER_CLASS
        message_type = RESOLVE_RESULT
        schema_class = "ResolveDidResultSchema"

    def __init__(
        self,
        *,
        sent_time: Union[str, datetime] = None,
        did_document: str = None,
        localization: str = None,
        **kwargs,
    ):
        """
        TODO: update doc
        Initialize basic message object.
        Args:
            sent_time: Time message was sent
            did_document: did document (as json or python object)
            localization: localization
        """
        super().__init__(**kwargs)
        if not sent_time:
            sent_time = datetime_now()
        if localization:
            self._decorators["l10n"] = localization
        self.sent_time = datetime_to_str(sent_time)
        if not isinstance(did_document, str):
            did_document = json.dumps(did_document)
        self.did_document = did_document


class ResolveDidResultSchema(AgentMessageSchema):
    """Basic message schema class."""

    class Meta:
        """Resolve DID message schema metadata."""

        model_class = ResolveDidResult

    sent_time = fields.Str(
        required=False,
        description="Time message was sent, ISO8601 with space date/time separator",
        **INDY_ISO8601_DATETIME,
    )
    example = '{"@context": "https://w3id.org/did/v0.11", "id": "did:sov:xyz",}'
    did_document = fields.Str(required=True, description="DID",
                              example=example)


class ResolveDidHandler(BaseHandler):
    """Message handler class for resolving did messages."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """
        Message handler logic for resolving a did.

        Args:
            context: request context
            responder: responder callback
        """
        self._logger.debug("ResolveDidHandler called with context %s", context)
        assert isinstance(context.message, ResolveDid)

        self._logger.info("Received resolve did: %s", context.message.did)

        resolver_url = context.settings.get("did_resolution_service")
        try:
            did_document = resolve_did(context.message.did, resolver_url)
        except Exception as err:
            self._logger.error(str(err))
            msg = (f"Could not resolve DID {context.message.did} using service"
                   f" {resolver_url}")
            raise HandlerException(msg)
        else:
            reply_msg = ResolveDidResult(did_document=did_document)
            reply_msg.assign_thread_from(context.message)
            if "l10n" in context.message._decorators:
                reply_msg._decorators["l10n"] = context.message._decorators["l10n"]
            await responder.send_reply(reply_msg)


def resolve_did(did, resolver_url):
    """Resolve a DID using the uniresolver.

    resolver_url has to contain a {did} field.
    """
    url = resolver_url.format(did=did)
    response = requests.get(url)
    if response.ok:
        content = response.json()
        return content['didDocument']
    raise HandlerException(f"Failed to resolve DID {did} using URL {url}")


class ResolveDidResultHandler(BaseHandler):
    """Message handler class for resolve did result messages."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """
        Message handler logic a did resolve result.

        Args:
            context: request context
            responder: responder callback
        """
        self._logger.debug("ResolveDidResultHandler called with context %s", context)
        assert isinstance(context.message, ResolveDidResult)

        self._logger.info("Received resolve did document")
        self._logger.debug("did document: %s", context.message.did_document)

        did_document = json.loads(context.message.did_document)

        await responder.send_webhook(
            "resolve_did_result",
            {
                "connection_id": context.connection_record.connection_id,
                "message_id": context.message._id,
                "did_document": did_document,
                "state": "received",
            },
        )

