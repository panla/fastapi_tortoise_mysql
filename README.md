# README

> 对异步框架 FastAPI，异步ORM Tortoise-orm，和 MySQL 数据库的综合demo

- [gitee](https://gitee.com/pankla/fastapi_tortoise_mysql)
- [github](https://github.com/panla/fastapi_tortoise_mysql)

## 环境

Python: 3.8

### venv 创建虚拟环境

```bash
mkdir venv && cd venv
python3 -m venv .
cd ../
pip install -r doc/requirements.txt[-i https://mirrors.aliyun.com/pypi/simple/]
```

### conda 创建虚拟环境

```bash
conda create -n name python=3.8
conda activate name
pip install -r doc/requirements.txt[-i https://mirrors.aliyun.com/pypi/simple/]
```

### 配置

- [.env 参考](./doc/config/env.example)
- [run.sh 参考](./doc/config/run.example.sh)

### 运行

```bash
uvicorn main:app --reload
uvicorn main:app --host='0.0.0.0' --port=8001 --reload
uvicorn main:app --host='0.0.0.0' --port=8001 --workers 1 --reload
uvicorn main:app --host='0.0.0.0' --port=8001 --workers 1 --loop=uvloop --http=httptools --reload

sh ./run.sh
```

### docker-compose

```bash
docker-compose up -d --build

docker-compose ps

docker-compose restart

docker-compose stop

docker-compose restart container_name
```

部署时文件结构

- project
  - conf
    - api
      - .env [参考](./doc/config/env.example)
      - `run.sh` [参考](./doc/config/run.example.sh)
    - mysql
      - my.cnf [参考](./doc/config/my.cnf)
  - data
    - api
      - logs
    - redis
      - data
    - mysql
      - data
  - api
    ...
  - docker-compose.yaml [参考](./doc/config/docker-compose.yaml)
