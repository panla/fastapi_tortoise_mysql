aerich upgrade
gunicorn main:app --bind 0.0.0.0:8000 --worker-class uvicorn.workers.UvicornWorker --workers 2 --worker-connections 10000 --log-level INFO --timeout 60