from typing import Dict

from fastapi import WebSocket


class Manager:
    _instance = None

    def __init__(self):
        self.active_connections: Dict[str: WebSocket] = dict()

    async def connect(self, socket_id: str, web_socket: WebSocket):
        await web_socket.accept()
        self.active_connections.update({socket_id: web_socket})

    def is_active(self, socket_id: str) -> bool:
        if socket_id in self.active_connections:
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
