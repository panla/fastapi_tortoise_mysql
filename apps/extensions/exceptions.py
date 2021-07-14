__all__ = [
    'BaseHTTPException', 'BadRequest', 'Unauthorized', 'Forbidden', 'NotFound', 'MethodNotAllowed',
]

from typing import Any, Optional, Dict

from starlette.exceptions import HTTPException

from apps.utils.define import StatusCode


class BaseHTTPException(HTTPException):
    STATUS_CODE = 400
    CODE = 40000
    MESSAGE = None

    def __init__(
            self,
            message: Any = None,
            status_code: int = 400,
            code: int = 40000,
            headers: Optional[Dict[str, Any]] = None
    ) -> None:
        self.message = message or self.MESSAGE
        self.status_code = status_code or self.STATUS_CODE
        self.code = code or self.CODE
        self.headers = headers

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, msg={self.message!r})"


class BadRequest(BaseHTTPException):
    STATUS_CODE = 400
    CODE = StatusCode.bad_request


class Unauthorized(BaseHTTPException):
    STATUS_CODE = 401
    CODE = StatusCode.unauthorized


class Forbidden(BaseHTTPException):
    STATUS_CODE = 403
    CODE = StatusCode.forbidden


class NotFound(BaseHTTPException):
    STATUS_CODE = 404
    CODE = StatusCode.not_found


class MethodNotAllowed(BaseHTTPException):
    STATUS_CODE = 405
    CODE = StatusCode.method_not_allowed
