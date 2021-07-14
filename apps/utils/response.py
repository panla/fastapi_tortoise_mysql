from typing import Any

from apps.utils import logger


def resp_success(message: str = '', data: Any = None):
    if message and message != 'success':
        logger.info(message)
    return {'status_code': 10000, 'message': message, 'data': data}
