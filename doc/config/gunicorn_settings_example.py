"""
gunicorn config example
reference resources
    https://docs.gunicorn.org/en/stable/settings.html
"""

bind = '0.0.0.0:8000'

workers = 2

worker_class = 'tools.worker.Worker'

worker_connections = 10000

timeout = 120

graceful_timeout = 20

keepalive = 20

loglevel = 'INFO'
