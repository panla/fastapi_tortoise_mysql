aerich upgrade
gunicorn main:app --bind 0.0.0.0:8000 --workers 2 --worker-class uvicorn.workers.UvicornWorker --worker-connections 10000 --timeout 120 --graceful-timeout 20 --keep-alive 20 --log-level INFO
# gunicorn main:app --config gunicorn_config.py
