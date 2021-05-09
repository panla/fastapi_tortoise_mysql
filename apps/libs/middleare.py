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


def register_middleware(app):

    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        response = await call_next(request)

        for middleware_code in middleware_codes:
            code = middleware_code.get('code')
            if response.status_code == code:
                content = {
                    'status_code': middleware_code.get('status_code'),
                    'message': middleware_code.get('message'),
                    'data': middleware_code.get('data', None)
                }
                return JSONResponse(content=content, status_code=code)
        return response
