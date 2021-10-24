__all__ = ['logger']

import os
import sys

from loguru import logger

from config import Config

LOG_LEVEL = Config.log.LOG_LEVEL
LOG_PATH = Config.log.LOG_PATH

os.makedirs(os.path.dirname(os.path.abspath(LOG_PATH)), exist_ok=True)

logger.remove()

logger.add(
    LOG_PATH, level=LOG_LEVEL.upper(), rotation="00:00", backtrace=True, diagnose=True, enqueue=True,
)
logger.add(sys.stdout, level=LOG_LEVEL.upper(), backtrace=True, diagnose=True, enqueue=True)
