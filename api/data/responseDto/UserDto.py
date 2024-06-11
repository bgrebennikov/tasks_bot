from dataclasses import dataclass


@dataclass
class UserDto:
    user_id: int
    username: str
    first_name: str
    last_name: str
    first_join: bool = True
    balance: float = 0.0
