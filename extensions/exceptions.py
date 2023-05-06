from typing import Optional, Any, Dict

from fastapi import status
from starlette.exceptions import HTTPException

from conf import StatusCode
from .schema import SchemaMixin


class BaseHTTPException(HTTPException):
    MESSAGE = None
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    CODE = StatusCode.BadRequest

    def __init__(
            self,
            message: Any = None,
            code: int = None,
            headers: Optional[Dict[str, Any]] = None
    ) -> None:
        self.message = message or self.MESSAGE
        self.status_code = self.STATUS_CODE
        self.code = code or self.CODE
        self.detail = self.message
        self.headers = headers

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}(status_code={self.status_code!r}, code={self.code}, msg={self.message!r})'

    def response(self):
        return SchemaMixin(code=self.code, message=self.message, data=None).dict()


class BadRequest(BaseHTTPException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    CODE = StatusCode.BadRequest


class Unauthorized(BaseHTTPException):
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    CODE = StatusCode.Unauthorized


class Forbidden(BaseHTTPException):
    STATUS_CODE = status.HTTP_403_FORBIDDEN
    CODE = StatusCode.Forbidden


class NotFound(BaseHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    CODE = StatusCode.NotFound


class MethodNotAllowed(BaseHTTPException):
    STATUS_CODE = status.HTTP_405_METHOD_NOT_ALLOWED
    CODE = StatusCode.MethodNotAllowed


class Locked(BaseHTTPException):
    STATUS_CODE = status.HTTP_423_LOCKED
    CODE = StatusCode.Locked
