import os
import sys

from loguru import logger

import config

__all__ = ['logger']


os.makedirs(os.path.dirname(os.path.abspath(config.LOG_PATH)), exist_ok=True)

logger.remove()

logger.add(config.LOG_PATH, level=config.LOG_LEVEL.upper(), backtrace=True, diagnose=True, enqueue=True)
logger.add(sys.stdout, level=config.LOG_LEVEL.upper(), backtrace=True, diagnose=True, enqueue=True)
