__all__ = ['logger']

import sys
from pathlib import Path

from loguru import logger

from config import LogConfig

LOG_LEVEL = LogConfig.LEVEL.upper()
Path(LogConfig.PATH).parent.mkdir(exist_ok=True)

logger.remove()
logger.add(
    LogConfig.PATH, level=LOG_LEVEL, rotation="00:00", backtrace=True, diagnose=True, enqueue=True, compression='tar.gz'
)
logger.add(sys.stdout, level=LOG_LEVEL, backtrace=True, diagnose=True, enqueue=True)
