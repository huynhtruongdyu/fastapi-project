from enum import Enum


class HttpStatusCode(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 502


def ResponseModel(data, message: str = 'successfully'):
    return {
        "data": data,
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code: HttpStatusCode, message: str = None, param: any = None):
    return {
        "error": error,
        "code": code,
        "message": message,
        "param": param
    }
