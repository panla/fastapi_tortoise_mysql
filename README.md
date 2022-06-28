# README

> A demo that use the async web frame work: FastAPI, async orm: Tortoise-ORM, the database: MySQL

- [![MIT licensed](https://img.shields.io/github/license/panla/fastapi_tortoise_mysql)](https://raw.githubusercontent.com/panla/fastapi_tortoise_mysql/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/panla/fastapi_tortoise_mysql.svg)](https://github.com/panla/fastapi_tortoise_mysql/stargazers) [![GitHub forks](https://img.shields.io/github/forks/panla/fastapi_tortoise_mysql.svg)](https://github.com/panla/fastapi_tortoise_mysql/network)
- [![github](https://img.shields.io/badge/fastapi__tortoise__mysql-github-red)](https://github.com/panla/fastapi_tortoise_mysql) [![gitee](https://img.shields.io/badge/fastapi__tortoise__mysql-gitee-red)](https://gitee.com/pankla/fastapi_tortoise_mysql)

## keywords

- ![python-3.9](https://img.shields.io/badge/python-3.9-yellowgreen) ![python-asyncio](https://img.shields.io/badge/python-asyncio-green)
- [![FastAPI](https://img.shields.io/badge/tiangolo-FastAPI-green)](https://github.com/tiangolo/fastapi) [![pydantic](https://img.shields.io/badge/samuelcolvin-pydantic-green)](https://github.com/samuelcolvin/pydantic) [![tortoise-orm](https://img.shields.io/badge/tortoise-Tortoise--ORM-yellowgreen)](https://github.com/tortoise/tortoise-orm)
- ![MySQL](https://img.shields.io/badge/MySQL-8-yellowgreen) [![Redis](https://img.shields.io/badge/Redis-6.2-red)](https://redis.io/)
- ![MQTT](https://img.shields.io/badge/MQTT-V5-orange) [![Celery](https://img.shields.io/badge/Celery-V5-orange)](https://docs.celeryproject.org/en/stable/)

## environment

- [require packets for work](./mirrors/requirements.txt)
- [require packets for dev and test](./mirrors/requirements-dev.txt)

## command

```bash
# test
make test

CODE_ENV=test pytest --rootdir ./tests -s

# run
make run
```

## dir and file

### project file

- [MIT LICENSE](./LICENSE)
- [A Global Config File](./config.py)
- [Dir or File for Using Cython cythonize](./build.txt)
- [The Program Entry File](./server.py)
- [Dockerfile](./Dockerfile)
- [Makefile](./Makefile)
- [The Conf File of Aerich](./pyproject.toml)
- [The Change Log of Different Version for This Project](./CHANGELOG.md)

### some tools

- [The Script of Create Blank migration SQL File](./tools/create_migration_template_file.py)
- [The Script of Find Target in some Dirs](./tools/find.py)
- [The Script of Insert Some Data Into Database](./tools/insert_data.py)
- [The Extend uvicorn Worker](./tools/worker.py)

## deploy and dir

### build and run

```bash
# download docker and docker-compose

# create docker network: example
docker network create --driver bridge --subnet xxxxxx --gateway xxxxx xxxxxxxx

# mkdir project dir
mkdir /srv/project && cd /srv/project && mkdir conf/fastapi_tm_api conf/fastapi_tm_db conf/fastapi_tm_redis -p

# clone source code
git clone this api fastapi_tm_api

## edit config settings
# reference resources ./docs/deploy/docker-compose.yaml
touch docker-compose.yaml

# reference resources ./docs/deploy/my.cnf
touch conf/fastapi_tm_db/my.cnf

# reference resources ./conf/product.toml ./conf/test.toml
touch conf/fastapi_tm_api/product.local.toml
touch conf/fastapi_tm_api/test.local.toml

# reference resources ./docs/deploy/gunicorn_settings_example.py
touch conf/fastapi_tm_api/gunicorn_config.py

# reference resources ./docs/deploy/docker-entrypoint.sh
touch conf/fastapi_tm_api/docker-entrypoint.sh

# build and start
docker-compose up -d --build
```

### the project dir example

```text
.
├── api
├── conf
│   ├── fastapi_tm_api
│   │   ├── product.local.toml
│   │   ├── test.local.toml
│   │   ├── docker-entrypoint.sh
│   │   └── gunicorn_config.py
│   ├── fastapi_tm_db
│   │   └── my.cnf
│   └── fastapi_tm_redis
│       └── redis.conf
├── data
│   ├── fastapi_tm_db
│   │   └── data
│   └── fastapi_tm_redis
│       └── data
│           └── dump.rdb
├── docker-compose.yaml
└── logs
    ├── fastapi_tm_api
    │   └── x.log
    └── fastapi_tm_celery
```
