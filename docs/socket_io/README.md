# README

一个 借助 `python-socketio` 实现的 socket.io demo

## require package

```bash
# for server
pip install python-socketio fastapi uvicorn

# for sync client
pip install "python-socketio[client]"

# for async client
pip install "python-socketio[asyncio_client]"
```

## run

```bash
python server.py --help

python client.py --help
```
