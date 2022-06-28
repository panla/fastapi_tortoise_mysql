aerich upgrade

# gunicorn main:app --config gunicorn_config.py
gunicorn server:app --bind 0.0.0.0:8000 --workers 2 --worker-class uvicorn.workers.UvicornWorker --timeout 120 --graceful-timeout 20 --keep-alive 20 --log-level INFO
# --worker-connections 10000

# uvicorn server:app --workers 2 --reload
