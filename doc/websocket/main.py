import time

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from .html_string import html_a, html_b
from .manager import Manager
from .redis_client import RedisClient


app = FastAPI()
manager = Manager()


@app.get("/ws_a/html")
async def get():
    return HTMLResponse(html_a)


@app.get("/ws_b/html")
async def get():
    return HTMLResponse(html_b)


@app.websocket("/ws_a/{client_id}")
async def websockets_endpoint(web_socket: WebSocket, client_id: int):
    try:
        print(web_socket.headers)
        await manager.connect(str(client_id), web_socket)
        web_socket.socket_id = client_id
        data = await web_socket.receive_text()
        print(data)
        while True:
            if str(client_id) in manager.active_connections:
                redis_client = RedisClient(data)

                value = await redis_client.lpop(data)
                time.sleep(0.5)
                if value:
                    await manager.send_single_message(f"Client #{client_id} says: {data}", str(client_id))
                    await manager.send_single_message(f'Server says: {value}', str(client_id))
            else:
                print('active_connections 中没有此连接')
                break

    except WebSocketDisconnect:
        print('异常，关闭连接')
        await manager.disconnect(str(client_id))


@app.websocket("/ws_b/{client_id}")
async def websockets_endpoint2(web_socket: WebSocket, client_id: int):
    await manager.connect(str(client_id), web_socket)
    try:
        print(web_socket.headers)
        web_socket.socket_id = client_id
        receive_data = await web_socket.receive_text()
        print(receive_data)
        while True:
            if str(client_id) in manager.active_connections:
                send_data = receive_data * 2
                time.sleep(0.5)
                await manager.send_single_message(f"Client #{client_id} send: {receive_data}", str(client_id))
                await manager.send_single_message(f'Server response: {send_data}', str(client_id))
            else:
                print('active_connections 中没有此连接')
                break

    except WebSocketDisconnect:
        print('异常，关闭连接')
        await manager.disconnect(str(client_id))


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
