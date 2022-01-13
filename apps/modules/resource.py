from typing import Union

from tortoise.queryset import MODEL

from extensions import NotFound


class ResourceOp:
    def __init__(self, model, pk: Union[str, int]):
        self.model: 'MODEL' = model
        self.pk = pk

    async def instance(self, is_delete: bool = None):

        _instances = self.model.filter(id=self.pk)
        if is_delete is not None:
            _instances = _instances.filter(is_delete=is_delete)

        _instance = await _instances.first()

        if not _instance:
            raise NotFound(message=f'Model = {self.model.__name__}, pk = {self.pk} is not exists')
        return _instances, _instance
