from enum import Enum


class RequestMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    OPTIONS = 'OPTIONS'
    UPDATE = 'UPDATE'
