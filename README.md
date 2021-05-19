# README

> 对异步框架 FastAPI，异步ORM Tortoise-orm，和 MySQL 数据库的综合demo

- [gitee](https://gitee.com/pankla/fastapi_tortoise_mysql)
- [github](https://github.com/panla/fastapi_tortoise_mysql)

## 环境

Python: 3.8.8

### 创建虚拟环境

```bash
mkdir venv && cd venv
python3 -m venv .
cd ../
```

### 激活虚拟环境并安装第三方库

```bash
source venv/bin/activate

pip3 install -r doc/requirements.txt [-i https://pypi.tuna.tsinghua.edu.cn/simple]
```

## 配置

- [.env](doc/config/env.example)
- [run.sh](doc/run.example.sh)
- [tortoise_conf_test_example.py](doc/config/tortoise_conf_test_example.py)

## 数据库

[aerich参考](doc/db/aerich.md)

## swagger文档

```text
/api/v1/admin/docs
/api/v1/admin/redoc
```

## 运行

```bash
uvicorn main:app
uvicorn main:app --reload
uvicorn main:app --host='127.0.0.1' --port=8000 --reload

# 参考 doc/run.example.sh
sh run.sh
```

## 部署

[参考](doc/deploy)
