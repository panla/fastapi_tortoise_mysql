import os
import logging
from logging.handlers import TimedRotatingFileHandler

from fastapi import FastAPI
from fastapi.logger import logger

import config


def set_logger_handle(app: FastAPI):
    """配置 logger handle"""

    log_level = config.LOG_LEVEL.upper()
    logfile_path = config.LOG_PATH

    os.makedirs(os.path.dirname(logfile_path), exist_ok=True)

    file_handler = TimedRotatingFileHandler(logfile_path, 'midnight')
    file_handler.setLevel(level=log_level)
    file_handler.setFormatter(
        logging.Formatter('[%(asctime)s>] [%(levelname)s] <-%(filename)s-line %(lineno)d>  %(message)s')
    )
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    app.logger = logger
