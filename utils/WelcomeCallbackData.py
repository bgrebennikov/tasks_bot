from enum import Enum


class WelcomeCallbackData(Enum):

    def __str__(self):
        return str(self.value)

    ADVERTISER = "ADVERTISER"
    WORKER = "WORKER"
