import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(BASE_DIR.absolute()))

from apps.application import create_app
from config import ORM_TEST_MIGRATE_CONF
from apps.models import User, AdminUser, Book, Car, Order, Phone, Question
from config import AuthenticConfig, ORM_TEST_MIGRATE_CONF
from extensions import NotFound, BadRequest
from services.redis_ext import TokenRedis
from apps.modules import TokenResolver
