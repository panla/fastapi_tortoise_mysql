__all__ = ['logger']

import os
import sys

from loguru import logger

from config import Config

os.makedirs(os.path.dirname(os.path.abspath(Config.LOG_PATH)), exist_ok=True)

logger.remove()

logger.add(
    Config.LOG_PATH, level=Config.LOG_LEVEL.upper(), rotation="00:00", backtrace=True, diagnose=True, enqueue=True,
)
logger.add(sys.stdout, level=Config.LOG_LEVEL.upper(), backtrace=True, diagnose=True, enqueue=True)
