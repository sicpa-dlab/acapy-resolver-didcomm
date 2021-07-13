from enum import Enum


class ConnectionsState(str, Enum):
    INIT = "init"
    START = "start"
    ERROR = "error"
    ACTIVE = "active"
    INVITATION = "invitation"
    REQUEST = "request"
    RESPONSE = "response"
    COMPLETED = "completed"
    ABANDONED = "abandoned"

    def __str__(self) -> str:
        return str(self.value)
