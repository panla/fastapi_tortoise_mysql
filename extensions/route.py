from json import JSONDecodeError

from fastapi import Request
from fastapi.routing import APIRoute

from extensions import logger


class Route(APIRoute):
    """Extension Route and log request.json()"""

    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def log_request_detail(request: Request):

            logger.info(f'{request.method} {request.url}'.center(80, '*'))

            methods = ['POST', 'PUT', 'PATCH']
            content_type = request.headers.get('content-type', '')

            if request.method in methods and 'application/json' in content_type:
                try:
                    payload = await request.json()
                    if payload:
                        logger.info(payload)
                except JSONDecodeError:
                    logger.error('encounter JSONDecodeError')
                except UnicodeDecodeError:
                    logger.error('encounter UnicodeDecodeError')
            return await original_route_handler(request)

        return log_request_detail
