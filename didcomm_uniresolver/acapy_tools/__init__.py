"""Tools for working with ACA-Py as a plugin."""

from aries_cloudagent.messaging.base_handler import BaseHandler
from aries_cloudagent.messaging.responder import BaseResponder
from aries_cloudagent.messaging.agent_message import AgentMessageSchema
from aries_cloudagent.messaging.request_context import RequestContext
from aries_cloudagent.messaging.models.base import BaseModel, BaseModelSchema


def expand_message_class(cls):
    """Class decorator for removing boilerplate of AgentMessages."""
    # pylint: disable=protected-access

    if not hasattr(cls, "message_type"):
        raise ValueError(
            "Expected value message_type not found on class {}".format(cls.__name__)
        )
    if not hasattr(cls, "Fields") and not hasattr(cls, "fields_from"):
        raise ValueError(
            "Class {} must have nested class Fields or schema defining expected fields".format(
                cls.__name__
            )
        )

    cls.Meta = type(
        cls.__name__ + ".Meta",
        (),
        {
            "__module__": cls.__module__,
            "message_type": cls.message_type,
            "schema_class": cls.__name__ + ".Schema",
        },
    )

    fields = {}
    if hasattr(cls, "Fields"):
        fields.update(
            {
                var: getattr(cls.Fields, var)
                for var in vars(cls.Fields)
                if not var.startswith("__")
            }
        )
    if hasattr(cls, "fields_from"):
        fields.update(cls.fields_from._declared_fields)

    cls.Schema = type(
        cls.__name__ + ".Schema",
        (AgentMessageSchema,),
        {"__module__": cls.__module__, **fields},
    )
    cls.__slots__ = list(fields.keys())
    cls.Schema.Meta = type(
        cls.Schema.__name__ + ".Meta",
        (),
        {"__module__": cls.__module__, "model_class": cls},
    )
    cls._get_schema_class = lambda: cls.Schema

    if hasattr(cls, "protocol") and cls.protocol:
        cls.Meta.message_type = "{}/{}".format(cls.protocol, cls.message_type)
        cls._type = property(fget=lambda self: self.Meta.message_type)

    if hasattr(cls, "handle"):
        cls.Handler = handler(cls.handle)
        cls._get_handler_class = lambda: cls.Handler
    elif hasattr(cls, "handler"):
        cls.Meta.handler_class = cls.handler
    else:
        cls._get_handler_class = lambda: cls.Handler

    return cls


def expand_model_class(cls):
    """Class decorator for removing boilerplate from BaseModels."""
    if not hasattr(cls, "Fields") and not hasattr(cls, "fields_from"):
        raise ValueError(
            "Class {} must have nested class Fields or schema defining expected fields".format(
                cls.__name__
            )
        )

    if hasattr(cls, "Meta") and cls.Meta != BaseModel.Meta:
        cls.Meta.schema_class = cls.__name__ + ".Schema"
    else:
        cls.Meta = type(
            cls.__name__ + ".Meta",
            (),
            {"__module__": cls.__module__, "schema_class": cls.__name__ + ".Schema"},
        )

    fields = {}
    if hasattr(cls, "Fields"):
        fields.update({var: getattr(cls.Fields, var) for var in vars(cls.Fields)})
    if hasattr(cls, "fields_from"):
        fields.update(cls.fields_from._declared_fields)

    cls.Schema = type(
        cls.__name__ + ".Schema",
        (BaseModelSchema,),
        {"__module__": cls.__module__, **fields},
    )
    cls.__slots__ = list(fields.keys())
    cls.Schema.Meta = type(
        cls.Schema.__name__ + ".Meta",
        (),
        {"__module__": cls.__module__, "model_class": cls},
    )

    if hasattr(cls, "unknown"):
        cls.Schema.Meta.unknown = cls.unknown

    cls._get_schema_class = lambda: cls.Schema

    return cls


def handler(func):
    """Function decorator for creating Python handler classes."""

    class Handler(BaseHandler):
        __doc__ = func.__doc__
        __name__ = func.__name__
        __module__ = func.__module__

        @property
        @classmethod
        def load_path(cls):
            """Return load path for this handler."""
            return f"{cls.__module__}.{cls.__name__}"

        async def handle(self, context: RequestContext, responder: BaseResponder):
            """Handle message."""
            return await func(context.message, context, responder)

    return Handler


def generic_init(instance, **kwargs):
    """Initialize from kwargs into slots."""
    for slot in instance.__slots__:
        setattr(instance, slot, kwargs.get(slot))
        if slot in kwargs:
            del kwargs[slot]
    super(type(instance), instance).__init__(**kwargs)


def with_generic_init(cls):
    """Class decorator for adding generic init method."""
    cls.__init__ = generic_init
    return cls
