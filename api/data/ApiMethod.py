from dataclasses import dataclass

from api.data.RequestMethod import RequestMethod


@dataclass
class ApiMethod:
    method: str
    type: RequestMethod
    params: dict
