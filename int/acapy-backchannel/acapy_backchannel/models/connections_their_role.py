from enum import Enum


class ConnectionsTheirRole(str, Enum):
    INVITEE = "invitee"
    REQUESTER = "requester"
    INVITER = "inviter"
    RESPONDER = "responder"

    def __str__(self) -> str:
        return str(self.value)
