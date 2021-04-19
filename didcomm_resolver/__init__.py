"""DIDCOMM Universal Resolver Plugin for ACA-Py"""

import logging

from aries_cloudagent.config.injection_context import InjectionContext
from .resolver import DIDCommResolver

LOGGER = logging.getLogger(__name__)

__all__ = ["DIDCommResolver"]


async def setup(context: InjectionContext):
    """Setup the plugin."""

    LOGGER.error(
        """You must select a role. If you intend only to act as a
resolver over DIDComm, use didcomm_resolver.role.resolver.
If you intend only to resovle through a remote resolver over
DIDComm, use didcomm_resolver.role.requester."""
    )
