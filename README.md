# README

> a demo that use the async web_frame_work FastAPI, async orm tortoise-orm, the database MySQL

- <https://github.com/panla/fastapi_tortoise_mysql>
- <https://gitee.com/pankla/fastapi_tortoise_mysql>

## environment

Python: 3.8

## test

```bash
CODE_ENV=test pytest --rootdir ./tests -s

sh ./run_test.sh
```

## run

### build and deploy by docker-compose

```bash
# download docker and docker-compose

# create docker network: example
docker network create --driver bridge --subnet 172.22.0.0/16 --gateway 172.22.0.1 fastapi_net

# mkdir project dir
mkdir /srv/project && cd /srv/project && mkdir conf/api conf/mysql -p

# clone source code
git clone this api

## edit config settings
# reference resources ./doc/config/docker-compose.yaml
touch docker-compose.yaml

# reference resources ./doc/config/my.cnf
touch conf/mysql/my.cnf

# reference resources ./doc/config/env.example
touch conf/api/.env

# reference resources ./doc/config/gunicorn_settings_example.py
touch conf/api/gunicorn_config.py

# reference resources ./doc/config/run.example.sh
touch conf/api/run.sh

# build and start
docker-compose up -d --build
```

## the project dir example

```text
project
    ├── api
    │   ├── ...
    ├── conf
    │   ├── api
    │   │   ├── .env
    │   │   ├── gunicorn_config.py
    │   │   └── run.sh
    │   └── mysql
    │       └── my.cnf
    ├── data
    │   ├── mysql
    │   │   └── data
    │   └── redis
    │       └── data
    │           └── dump.rdb
    ├── docker-compose.yml
    ├── logs
    │   └── api
```
