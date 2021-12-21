# ChangeLog

[toc]

## 0.6

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
