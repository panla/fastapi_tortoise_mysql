from typing import Any

from extensions import logger


def resp_success(code: int = 10000, message: str = '', print_msg: str = '', data: Any = None) -> dict:
    if print_msg:
        pass
    else:
        if message and message != 'success':
            print_msg = message

    if print_msg:
        logger.info(print_msg)

    return {'code': code, 'message': message, 'data': data}
