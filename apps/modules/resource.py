from extensions import NotFound


class ResourceOp():
    def __init__(self, model, pk):
        self.model = model
        self.pk = pk

    async def instance(self, is_delete=None):
        if is_delete is not None:
            _instance = await self.model.filter(id=self.pk, is_delete=is_delete).first()
        else:
            _instance = await self.model.filter(id=self.pk).first()
        if not _instance:
            raise NotFound(message=f'Model = {self.model.__name__}, pk = {self.pk} is not exists')
        return _instance
