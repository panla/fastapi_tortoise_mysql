/opt/python/bin/aerich upgrade
/opt/python/bin/uvicorn main:app --host='0.0.0.0' --port=8000 --workers 2 --loop=uvloop --http=httptools --reload