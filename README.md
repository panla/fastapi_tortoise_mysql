# README

> 对异步框架FastAPI，异步ORM Tortoise-orm，和 MySQL 数据库的综合demo

## 环境

Python: 3.7

### 创建虚拟环境

```bash
mkdir venv && cd venv
python3 -m venv .
```

```bash
source venv/bin/activate

pip3 install -r doc/requirements.txt [-i https://pypi.tuna.tsinghua.edu.cn/simple]
```

## 配置

[config.py](doc/config.example.py)

## 数据库

[aerich](doc/aerich.md)

```bash
aerich upgrade
```

## 运行

```bash
uvicorn main:app
uvicorn main:app --reload
uvicorn main:app --host='127.0.0.1' --port=8000

# 参考 doc/run.example.sh
sh run.sh
```
