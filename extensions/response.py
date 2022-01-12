from typing import Any

from extensions import logger

from conf.const import StatusCode




def resp_success(message: str = '', print_msg: str = '', data: Any = None):
    if print_msg:
        pass
    else:
        if message and message != 'success':
            print_msg = message

    if print_msg:
        logger.info(print_msg)

    return {'message': message, 'data': data}
