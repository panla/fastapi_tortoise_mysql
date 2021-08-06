import socketio


class NameSpaceIO(socketio.AsyncNamespace):

    def on_connect(self, sid, *args, **kwargs):
        print(f'{sid} connect')

    def on_disconnect(self, sid):
        print(f'{sid} disconnect')

    async def on_join_room(self, sid, data: dict, *args, **kwargs):
        room = data.get('room', '1')
        print(f'{sid} join room {room}')

        data['num'] += 1

        self.enter_room(sid=sid, room=room, namespace=self.namespace)

        print(f'sid = {sid}, enter room room = {room}')

        await self.emit(event='response', data=data, room=room, namespace=self.namespace)

    def on_leave_room(self, sid, data: dict, *args, **kwargs):
        room = data.get('room', '1')
        print(f'{sid} leave room {room}')

        self.leave_room(sid=sid, room=room, namespace=self.namespace)

    async def on_my_event(self, sid, data: dict, *args, **kwargs):
        room = data.get('room', '1')
        print(f'sid = {sid}, on my event, room = {room}, receive data: ', data)

        await self.emit(event='response', data=data, room=room, namespace=self.namespace)
