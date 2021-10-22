import socketio

from extensions import logger


class NameSpaceSIO(socketio.AsyncNamespace):

    def on_connect(self, sid, *args, **kwargs):
        logger.info(f'sid = {sid} namespace = {self.namespace} connect')

    def on_disconnect(self, sid):
        self.disconnect(sid=sid)
        logger.info(f'sid = {sid} namespace = {self.namespace} disconnect')

    async def on_join_room(self, sid, data: dict):
        room = data.get('room')
        if not room:
            logger.info(f'sid = {sid}, not get room param')
            return await self.disconnect(sid=sid)

        logger.info(f'sid = {sid}, start enter room, room = {room}')
        logger.info(f'receive: {data}')

        self.enter_room(sid=sid, room=room)

        logger.info(f'sid = {sid}, enter room success, room = {room}')

        await self.emit(event='response', data=data, room=room)

    def on_leave_room(self, sid, data: dict):
        room = data.get('room')
        if room:
            room_lis = [room]
        else:
            room_lis = self.rooms(sid=sid)

        for room in room_lis:
            logger.info(f'sid = {sid} leave room, room = {room}')

            self.leave_room(sid=sid, room=room)

    async def on_my_event(self, sid, data: dict):
        room = data.get('room')
        if not room:
            return await self.disconnect(sid=sid)

        logger.info(f'sid = {sid}, my event, room = {room}')
        logger.info(f'receive: {data}')

        await self.emit(event='response', data=data, room=room)
