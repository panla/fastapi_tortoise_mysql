from json import JSONDecodeError

from fastapi import Request
from fastapi.routing import APIRoute

from extensions import logger


class Route(APIRoute):
    """Extension Route and log request.json()"""

    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def log_request_detail(request: Request):

            logger.info('start request'.center(60, '*'))
            logger.info(f'{request.method} {request.url}')
            if (
                    request.method in ['POST', 'PUT', 'PATCH']
                    and request.headers.get('content-type') == 'application/json'
            ):
                try:
                    params = await request.json()
                    if params:
                        logger.info(params)
                except JSONDecodeError:
                    logger.error('encounter JSONDecodeError')
                except UnicodeDecodeError:
                    logger.error('encounter UnicodeDecodeError')
            logger.info('end request'.center(60, '*'))
            return await original_route_handler(request)

        return log_request_detail
