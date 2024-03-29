import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from conf.const import StatusCode

# don`t overwrite custom extension Exception and StatusCode
# example, already had raised and catch 404, don`t define 404

MiddlewareCodeContents = {
    405: {'code': StatusCode.MethodNotAllowed, 'message': 'METHOD_NOT_ALLOWED', 'data': None},
    406: {'code': StatusCode.NotAcceptable, 'message': 'NOT_ACCEPTABLE', 'data': None},
    408: {'code': StatusCode.RequestTimeout, 'message': 'REQUEST_TIMEOUT', 'data': None},
    411: {'code': StatusCode.LengthRequired, 'message': 'LENGTH_REQUIRED', 'data': None},
    413: {'code': StatusCode.EntityTooLarge, 'message': 'REQUEST_ENTITY_TOO_LARGE', 'data': None},
    414: {'code': StatusCode.RequestUriTooLong, 'message': 'REQUEST_URI_TOO_LONG', 'data': None},
    431: {
        'code': StatusCode.HeaderFieldsTooLarge,
        'message': 'REQUEST_HEADER_FIELDS_TOO_LARGE',
        'data': None
    }
}


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

    app.add_middleware(
        GZipMiddleware,
        minimum_size=500,
        compresslevel=9
    )


def register_middleware(app: FastAPI):
    @app.middleware('http')
    async def rewrite_other_exception_response(request: Request, call_next):
        """overwrite response"""

        start_time = time.time()
        response = await call_next(request)

        m_content = MiddlewareCodeContents.get(response.status_code, None)
        if m_content:
            return JSONResponse(content=m_content, status_code=response.status_code)

        response.headers['X-Process-Time'] = str((time.time() - start_time) * 1000)
        return response
