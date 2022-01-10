import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from extensions import middleware_code_contents


def register_cross(app: FastAPI):
    """deal Cross Origin Resource Sharing"""

    app.add_middleware(
        CORSMiddleware,
        allow_methods=['*'],
        allow_headers=['*'],
        allow_credentials=True,
        allow_origin_regex='https?://.*',
        expose_headers=['X-TOKEN', 'X-Process-Time']
    )


def register_middleware(app: FastAPI):
    @app.middleware("http")
    async def rewrite_other_exception_response(request: Request, call_next):
        """overwrite response"""

        start_time = time.time()
        response = await call_next(request)

        m_content = middleware_code_contents.get(response.status_code, None)
        if m_content:
            return JSONResponse(content=m_content, status_code=response.status_code)

        response.headers['X-Process-Time'] = str((time.time() - start_time) * 1000)
        return response
