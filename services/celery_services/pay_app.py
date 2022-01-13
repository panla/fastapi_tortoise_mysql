"""
pip install celery==5.2.3
"""

from celery import Celery

from .config import CeleryConfig


app = Celery('tasks')

app.config_from_object(CeleryConfig)
