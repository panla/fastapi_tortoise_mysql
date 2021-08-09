import socketio

from apps.utils import logger


class NameSpaceSIO(socketio.AsyncNamespace):

    def on_connect(self, sid, *args, **kwargs):
        logger.info(f'{sid} connect')

    def on_disconnect(self, sid):
        logger.info(f'{sid} disconnect')

    async def on_join_room(self, sid, data: dict):
        room = data.get('room', '1')

        logger.info(f'sid = {sid}, join room, room = {room}')
        logger.info(f'receive: {data}')

        self.enter_room(sid=sid, room=room)

        logger.info(f'sid = {sid}, enter room, room = {room}')

        data['num'] += 1

        await self.emit(event='response', data=data, room=room)

    def on_leave_room(self, sid, data: dict):
        room = data.get('room', '1')

        logger.info(f'{sid} leave room {room}')

        self.leave_room(sid=sid, room=room)

    async def on_my_event(self, sid, data: dict):
        room = data.get('room', '1')

        logger.info(f'sid = {sid}, my event, room = {room}')
        logger.info(f'receive: {data}')

        data['num'] += 1

        await self.emit(event='response', data=data, room=room)
