from fastapi import HTTPException


class UnauthorizedException(HTTPException):
    pass


class ForbiddenException(HTTPException):
    pass


class NotFoundException(HTTPException):
    pass


class MethodNotAllowedException(HTTPException):
    pass
