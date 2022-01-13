from celery import Celery


class CeleryProxy:

    def __init__(self, app: Celery) -> None:
        self.app = app

    def send_tasks(self, *args, **kwargs):
        return self.app.send_task(*args, **kwargs)
