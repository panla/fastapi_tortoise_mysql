# README

> a demo that use the async web frame work: FastAPI, async orm: tortoise-orm, the database: MySQL

- <https://github.com/panla/fastapi_tortoise_mysql>
- <https://gitee.com/pankla/fastapi_tortoise_mysql>

## tags

- *asyncio*
- *fastapi*
- *tortoise-orm*
- *MySQL*
- *Redis*
- *socket.io*
- *websockets*

## environment

- Python: 3.8

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

- [license](./LICENSE)
- [a global config file](./config.py)
- [dir or file for using Cython cythonize](./build.txt)
- [the program entry file](./main.py)
- [Dokerfile](./Dockerfile)
- [Makefile](./Makefile)
- [the conf file of aerich](./aerich.ini)
- [the conf file oh aerich, new](./pyproject.toml)
- [the different version`s change log record for this project](./CHANGELOG.md)
- [the config of pytest](./pytest.ini)

### some tools

- [the script of create blank migration sql file](./tools/create_migration_template_file.py)
- [the script of find target in some dirs](./tools/find.py)
- [the script of insert some data into database](./tools/insert_data.py)
- [the extend worker](./tools/worker.py)

## deploy and dir

### build and run

```bash
# download docker and docker-compose

# create docker network: example
docker network create --driver bridge --subnet 172.22.0.0/16 --gateway 172.22.0.1 fastapi_tm_net

# mkdir project dir
mkdir /srv/project && cd /srv/project && mkdir conf/api conf/mysql -p

# clone source code
git clone this api

## edit config settings
# reference resources ./docs/deploy/docker-compose.yaml
touch docker-compose.yaml

# reference resources ./docs/deploy/my.cnf
touch conf/mysql/my.cnf

# reference resources ./conf/product.toml ./conf/test.toml
touch conf/api/conf/product.local.toml
touch conf/api/conf/test.local.toml

# reference resources ./docs/deploy/gunicorn_settings_example.py
touch conf/api/gunicorn_config.py

# reference resources ./docs/deploy/docker-entrypoint.sh
touch conf/api/docker-entrypoint.sh

# build and start
docker-compose up -d --build
```

### the project dir example

```text
project
    ├── api
    │   ├── ...
    conf
    │   ├── api
    │   │   ├── conf
    │   │   │   ├── product.local.toml
    │   │   │   └── test.local.toml
    │   │   ├── docker-entrypoint.sh
    │   │   ├── gunicorn_config.py
    │   │   └── run.sh
    │   └── mysql
    │       ├── my.cnf
    │       └── sources.list
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

## other

- if use `socket.io`, don`t use gunicorn, but uvicorn
