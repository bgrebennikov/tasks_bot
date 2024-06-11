from enum import Enum


class WorkerCallbackData(Enum):
    GET_TASK = "GET_TASK"
    INVITE = "INVITE"
    SUPPORT = "SUPPORT"

    HOME = "HOME"

    CHECK_TASK = "CHECK_TASK"
    NEXT_TASK = "NEXT_TASK"

    WALLET = "WALLET"

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return str(self)
