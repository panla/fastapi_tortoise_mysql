__all__ = [
    'register_cross', 'register_middleware',
]

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from apps.utils import middleware_codes


def register_cross(app: FastAPI):
    """解决跨域"""

    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex='https?://.*',
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


def register_middleware(app: FastAPI):
    @app.middleware("http")
    async def rewrite_other_exception_response(request: Request, call_next):
        response = await call_next(request)

        middleware_code = middleware_codes.get(response.status_code, None)
        if middleware_code:
            return JSONResponse(content=middleware_code, status_code=response.status_code)
        return response
