import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from config import ORM_TEST_MIGRATE_CONF
from apps import create_app
from apps.extensions import NotFound
from apps.models import User, AdminUser, Book, Car, Order, Phone, Question
from apps.modules.token import encode_auth_token
