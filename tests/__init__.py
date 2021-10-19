import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from config import ORM_TEST_MIGRATE_CONF
from apps import create_app
from extensions import NotFound, BadRequest
from apps.models import User, AdminUser, Book, Car, Order, Phone, Question
from apps.modules import TokenResolver
