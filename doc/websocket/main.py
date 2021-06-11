from typing import List, Dict
import time

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Request
from aioredis import create_redis_pool

app = FastAPI()

redis_client = None


async def redis_pool():
    """redis 连接池"""

    global redis_client
    redis_uri = f"redis://:@127.0.0.1:6379/0?encoding=utf-8"

    pool = redis_client or await create_redis_pool(redis_uri)
    redis_client = pool
    return pool


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:18010/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class Manager:
    _instance = None

    def __init__(self):
        self.active_connections: Dict[str: WebSocket] = dict()

    async def connect(self, socket_id: str, web_socket: WebSocket):
        await web_socket.accept()
        self.active_connections.update({socket_id: web_socket})

    def is_active(self, socket_id) -> bool:
        if str(socket_id) in self.active_connections:
            return True
        return False

    async def disconnect(self, socket_id: str):
        connection = self.active_connections.pop(socket_id, None)
        if connection:
            await connection.close()

    async def send_single_message(self, message, socket_id: str):
        if self.is_active(socket_id):
            ws = self.active_connections.get(socket_id)
            await ws.send_text(message)

    async def broadcast(self, message: str):
        for _, web_socket in self.active_connections.items():
            await web_socket.send_text(message)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


manager = Manager()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websockets_endpoint(web_socket: WebSocket, client_id: int):
    try:
        print(web_socket.headers)
        print(web_socket.headers.get('sec-websocket-extensions'))
        await manager.connect(str(client_id), web_socket)
        web_socket.socket_id = client_id
        data = await web_socket.receive_text()
        print(data)
        while True:
            if str(client_id) in manager.active_connections:
                redis = await redis_pool()
                value = await redis.lpop(data)
                time.sleep(0.1)
                # print(client_id, time.time())
                if value:
                    await manager.send_single_message(f"Client #{client_id} says: {data}", web_socket)
                    await manager.send_single_message(f'Server says: {value}', web_socket)
                    await manager.send_single_message(f'Server says: {int(data) ** 2}', web_socket)
            else:
                print('active_connections 中没有此连接')
                break

    except WebSocketDisconnect:
        print('异常，关闭连接')
        await manager.disconnect(str(client_id))
        # await manager.broadcast(f"Client #{client_id} left the chat")


@app.post('/suspend/{client_id}')
async def suspend_websockets(client_id: int):
    if str(client_id) in manager.active_connections:
        await manager.disconnect(str(client_id))
    return {'message': 'success', 'status_code': 10201, 'data': None}


@app.get('/send_test/{client_id}')
async def send_test(client_id: int):
    ws = manager.active_connections.get(f'{client_id}')
    for i in range(100):
        await manager.send_single_message(f'Server says: {i}', ws)
    return {'success': True}
