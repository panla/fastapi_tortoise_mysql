# README

> a demo that use the async web_frame_work FastAPI, async orm tortoise-orm, the database MySQL

- <https://github.com/panla/fastapi_tortoise_mysql>
- <https://gitee.com/pankla/fastapi_tortoise_mysql>

## environment

Python: 3.8

### create virtual environment by venv

```bash
mkdir venv && cd venv
python3 -m venv .
cd ../
pip install -r doc/requirements.txt[-i https://mirrors.aliyun.com/pypi/simple/]
```

### create virtual environment by Anaconda/Miniconda

```bash
conda create -n name python=3.8
conda activate name
pip install -r doc/requirements.txt[-i https://mirrors.aliyun.com/pypi/simple/]
```

### settings example

- [.env example](./doc/config/env.example)
- [run.sh example](./doc/config/run.example.sh)
- [mysql my.cnf example](./doc/config/my.cnf)

## test

```bash
CODE_ENV=test pytest --rootdir ./tests -s

sh ./run_test.sh
```

## run

### start run by command

```bash
uvicorn main:app --reload
uvicorn main:app --host='0.0.0.0' --port=8001 --reload
uvicorn main:app --host='0.0.0.0' --port=8001 --workers 1 --reload
uvicorn main:app --host='0.0.0.0' --port=8001 --workers 1 --loop=uvloop --http=httptools --reload

sh ./run.sh
```

### build and deploy by docker-compose

```bash
docker-compose up -d --build

docker-compose ps

docker-compose restart

docker-compose stop

docker-compose restart container_name
```

the project dir example

- project
  - conf
    - api
      - .env [example](./doc/config/env.example)
      - `run.sh` [example](./doc/config/run.example.sh)
      - `gunicorn_config.py` [example](./doc/config/gunicorn_settings_example.py)
    - mysql
      - my.cnf [example](./doc/config/my.cnf)
  - data
    - api
    - redis
      - data
    - mysql
      - data
  - logs
    - api
  - api
    ...
  - docker-compose.yaml [example](./doc/config/docker-compose.yaml)
