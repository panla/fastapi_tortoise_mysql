import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

sys.path.append(BASE_DIR)

from config import AuthenticConfig, ORM_TEST_MIGRATE_CONF
from apps.application import create_app
from extensions import NotFound, BadRequest
from redis_ext import TokenRedis
from apps.models import User, AdminUser, Book, Car, Order, Phone, Question
from apps.modules import TokenResolver
