# ChangeLog

[toc]

## 0.7

### 0.7.5

- fix:
  - RedisSetting

### 0.7.4

- update/optimize
  - update MqttClient callback function
  - update README

- add
  - Redis Client Config Params

- fix
  - adapt new version PyJWT generate token

- requirements
  - upgrade fastapi from 0.85.0 to 0.87.0
  - upgrade cryptography from 37.0.4 to 38.0.1
  - upgrade PyJWT from 2.5.0 to 2.6.0
  - upgrade starlette from 0.20.4 to 0.21.0
  - upgrade uvicorn from 0.18.3 to 0.20.0
  - upgrade uvloop from 0.16.0 to 0.17.0
  - upgrade cryptography from 38.0.1 to 38.0.3
  - upgrade redis from 4.3.4 to 4.3.5
  - add httpx 0.23.1

### 0.7.3

- update/optimize
  - update log config

- add

- fix

- requirements
  - upgrade aiofiles from 0.8.0 to 22.1.0
  - upgrade cryptography from 37.0.4 to 38.0.1
  - upgrade fastapi from 0.78.0 to 0.85.0
  - upgrade httptools from 0.4.0 to 0.5.0
  - upgrade pydantic from 1.9.1 to 1.10.2
  - upgrade PyJWT from 2.4.0 to 2.5.0
  - upgrade starlette from 0.19.1 to 0.20.4
  - upgrade tortoise-orm from 0.19.1 to 0.19.2
  - upgrade uvicorn from 0.18.2 to 0.18.3
  - upgrade uvloop from 0.16.0 to 0.17.0

### 0.7.2

- update/optimize
  - optimize MqttClient comments and update variable name
  - optimize apps/api_admin/schemas/ optional fields

- add

- fix
  - BaseLockRedis error COMMENT

- requirements
  - upgrade uvicorn from 0.17.6  to 0.18.2
  - upgrade cryptography from 37.0.2 to 37.0.4
  - upgrade redis from 4.3.3 to 4.3.4

- dev requirements
  - upgrade requests from 2.27.1 to 2.28.1

- deploy
  - upgrade mysql from 8.0.26 to 8.0.29
  - upgrade rabbitmq from 3.8-management to 3.9-management

### 0.7.1

update/optimize

- update RedisClient method name
- rename main.py->server.py
- update MQTTClient comment
- update merge tools/ -> tools/cli.py
- upgrade image from python:3.9-slim-buster to python:3.9-slim-bullseye

add

- MQTTClient, add tls/ssl, add adapt v5

fix

- fix docs/deploy/docker-compose.yaml
- fix BaseRedis method

require packages

- add requirements
  - hiredis==2.0.0

- upgrade requirements-dev

## 0.6

### 0.6.11

update/optimize

add

fix

require packages

- upgrade requirements
  - fastapi==0.78.0
  - asyncmy==0.2.5
  - tortoise-orm==0.19.1
  - cryptography==37.0.2
  - passlib==1.7.4
  - PyJWT==2.4.0
  - redis==4.3.3
  - Cython==0.29.30
  - aerich==0.6.3
  - pytomlpp==1.0.11

- upgrade requirements-dev
  - pytest==7.1.2
  - celery==5.2.7

### 0.6.10

update/optimize

add

fix

require packages

- upgrade requirements
  - fastapi==0.75.0
  - uvicorn==0.17.6
  - asyncmy==0.2.4
  - tortoise-orm==0.19.0
  - cryptography==36.0.2

- upgrade requirements-dev
  - pytest==7.1.1
  - aiohttp==3.8.1
  - redis==4.2.0

### 0.6.9

update/optimize

- update celery config
- update pagesize -> page_size
- update Redis Connection Pool

add

fix

- fix redis pool when in test

require packages

- upgrade requestment
  - fastapi==0.74.1
  - loguru==0.6.0
  - uvicorn==0.74.5
  - Cython==0.29.28
  - httptools==0.4.0

- upgrade requirement-dev
  - pytest==7.0.1
  - redis==4.1.4

- add requirement-dev
- httpx==0.22.0

### 0.6.8

update/optimize

- update ResourceOp, update TypeHint
- update docker-compose api volumes
- update README
- entities->schemas resources->endpoints
- update config variable name

add

- supplement Python Type Hint
- add services, celery, mqtt

fix

- fix apps/modules/token.py query_user parameters error
- fix bug ResourceOp
- update settings.py add Optional
- fix use Redis

require packages

- add dev require packages
  - paho-mqtt==1.6.1
  - celery==5.2.3
  - redis==4.1.0
- upgrade dev require packages
  - requests==2.27.1
  - redis==4.1.1
- upgrade require packages
  - fastapi=0.72.0 and dependencies
  - aerich==0.6.2
  - tortoise-orm=0.18.1 and dependencies
  - uvicorn==0.17.0
  - aioredis==2.0.1
  - pytomlpp==1.0.10

### 0.6.7

update/optimize

- update config
- update define
- update import
- update variable, class, function name
- update project struct
- update response schema, error schema, exception, middleware
- update redis key`s method
- optimize code style
- update ModelMixin, BaseModel, cut useless code

add

- update README.md add data brand

fix

- fix Makefile
- fix tools.py
- fix common/tools.py
- fix ModelMixin variable name conflict

require packages

### 0.6.6

update/optimize

- update/optimize code
- update redis op
- file module
- update/new `status_code code`
- update `.dockerignore`
- remove some magic num

require packages

- aerich==0.6.0
- aiofiles==0.8.0
- uvicorn==0.16.0
- async-timeout==3.0.1
- cryptography==36.0.1
- Cython==0.29.26
- PyJWT==2.3.0
- pyparsing==3.0.6
- pytomlpp==1.0.9
- `typing_extensions`==4.0.1

remove

- remove `socket.io` module, require package, config
- Detach `socket.io` module to <https://github.com/panla/fastapi_sockets>

### 0.6.5

- update/optimize code
- optimize authentic
- update `socket.io` module
- upgrade require packages
  - python-socketio==5.5.0
  - python-engineio==4.3.0
  - websockets==10.1
- update deploy docs

### 0.6.4

- update create and verify token
- update dirs
- update api prefix `/api/v1/admin` -> `/api/admin`
- update encapsulation socket.io
- add socket.io test api
- update config settings and deploy docs
- add require package `pytomlpp`
- upgrade packages
  - fastapi==0.68.2

### 0.6.3

- upgrade require packet
  - `asyncmy`==0.2.3
- update redis ext and add resource lock
- update config.py add lru_cache
- update `v1_admin` logics func -> Class
- update tests
- update and add Makefile
- add build.txt and `__init__.py` to adapt Cython cythonize

### 0.6.2

- upgrade require package
  - PyJWT==2.2.0
  - cryptography==35.0.0
  - `httptools`==0.3.0
  - `tortoise-orm`==0.17.8
  - `uvicorn`==0.15.0
  - `uvloop`==0.16.0
- update Dockerfile

### 0.6.1

- upgrade require package
  - `tortoise-orm`==0.17.7
  - `aerich`==0.5.8
- fix pagination bug
- update and fix tests
- update config parameters

### 0.6.0

- update folder name and sorting distribution
- update doc
