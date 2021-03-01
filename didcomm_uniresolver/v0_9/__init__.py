"""DID Resolution Protocol v0.9 message and handler definitions."""

import json
import requests
import logging
from datetime import datetime
from typing import Union

from aries_cloudagent.messaging.base_handler import (
    BaseResponder, HandlerException, RequestContext
)
from marshmallow import fields

from aries_cloudagent.messaging.agent_message import AgentMessage
from aries_cloudagent.messaging.util import datetime_now, datetime_to_str
from aries_cloudagent.messaging.valid import INDY_ISO8601_DATETIME

from aries_cloudagent.protocols.didcomm_prefix import DIDCommPrefix

from ..acapy_tools import expand_message_class

LOGGER = logging.getLogger(__name__)

class DIDResolutionMessage(AgentMessage):
    """Base Message class for messages used for resolution."""
    protocol = "https://didcom.org/did_resolution/0.9"


@expand_message_class
class ResolveDid(DIDResolutionMessage):
    """Class defining the structure of a resolve did message."""
    message_type = "resolve"

    # TODO: add further response fields/options, see
    # https://github.com/hyperledger/aries-rfcs/tree/master/features/0124-did-resolution-protocol#resolve-message

    class Fields:
        sent_time = fields.Str(
            required=False,
            description="Time message was sent, ISO8601 with space date/time separator",
            **INDY_ISO8601_DATETIME,
        )
        did = fields.Str(required=True, description="DID",
                         example="did:sov:WRfXPg8dantKVubE3HX8pw",)

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


    @staticmethod
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


    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Resolve a DID in response to a resolve message.

        Args:
            context: request context
            responder: responder callback
        """
        LOGGER.debug("ResolveDidHandler called with context %s", context)
        assert isinstance(context.message, ResolveDid)

        LOGGER.info("Received resolve did: %s", context.message.did)

        resolver_url = context.settings.get("did_resolution_service")
        try:
            did_document = self.resolve_did(context.message.did, resolver_url)
        except Exception as err:
            LOGGER.error(str(err))
            msg = (f"Could not resolve DID {context.message.did} using service"
                   f" {resolver_url}")
            raise HandlerException(msg)
        else:
            reply_msg = ResolveDidResult(did_document=did_document)
            reply_msg.assign_thread_from(context.message)
            if "l10n" in context.message._decorators:
                reply_msg._decorators["l10n"] = context.message._decorators["l10n"]
            await responder.send_reply(reply_msg)


@expand_message_class
class ResolveDidResult(DIDResolutionMessage):
    """Class defining the structure of a resolve did message."""
    message_type = "resolve_result"

    class Fields:
        sent_time = fields.Str(
            required=False,
            description="Time message was sent, ISO8601 with space date/time separator",
            **INDY_ISO8601_DATETIME,
        )
        did_document = fields.Str(
            required=True,
            description="DID",
            example='{"@context": "https://w3id.org/did/v0.11", "id": "did:sov:xyz",}'
        )

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

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """
        Message handler logic a did resolve result.

        Args:
            context: request context
            responder: responder callback
        """
        LOGGER.debug("ResolveDidResultHandler called with context %s", context)
        assert isinstance(context.message, ResolveDidResult)

        LOGGER.info("Received resolve did document")
        LOGGER.debug("did document: %s", context.message.did_document)

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


MESSAGE_TYPES = DIDCommPrefix.qualify_all({
    msg_class.Meta.message_type: '{}.{}'.format(msg_class.__module__, msg_class.__name__)
    for msg_class in [
        ResolveDid,
        ResolveDidResult
    ]
})
