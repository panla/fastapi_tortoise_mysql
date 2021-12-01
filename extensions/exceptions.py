from typing import Optional, Any, Dict

from starlette.exceptions import HTTPException

from extensions import StatusCode


class BaseHTTPException(HTTPException):
    MESSAGE = None
    STATUS_CODE = 400
    CODE = 40000

    def __init__(
            self,
            message: Any = None,
            headers: Optional[Dict[str, Any]] = None
    ) -> None:
        self.message = message or self.MESSAGE
        self.status_code = self.STATUS_CODE
        self.detail = self.message
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


class Locked(BaseHTTPException):
    STATUS_CODE = 423
    CODE = StatusCode.locked
