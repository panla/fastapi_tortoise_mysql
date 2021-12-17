__all__ = ['logger']

import sys
from pathlib import Path

from loguru import logger

from config import LogConfig

LOG_LEVEL = LogConfig.LOG_LEVEL
LOG_PATH = LogConfig.LOG_PATH

Path(LOG_PATH).parent.mkdir(exist_ok=True)

logger.remove()

logger.add(
    LOG_PATH, level=LOG_LEVEL.upper(), rotation="00:00", backtrace=True, diagnose=True, enqueue=True,
)
logger.add(sys.stdout, level=LOG_LEVEL.upper(), backtrace=True, diagnose=True, enqueue=True)
