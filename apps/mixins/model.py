__all__ = [
    'BaseModel', 'ModelMixin',
]

from typing import Tuple

from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class BaseModel(Model):
    id = fields.BigIntField(pk=True, description='主键')
    created_at = fields.DatetimeField(auto_now_add=True, null=False, description='创建时间')
    updated_at = fields.DatetimeField(auto_now=True, null=False, description='更新时间')
    is_delete = fields.BooleanField(null=False, default=False, description='删除标识')

    class Meta:
        abstract = True

    class PydanticMeta:
        exclude = ('created_at', 'updated_at')


class ModelMixin(object):
    __slots__ = ()

    def __init__(self, **kwargs):
        pass

    @classmethod
    def ModelCreator(
            cls,
            exclude: Tuple[str, ...] = (),
            include: Tuple[str, ...] = (),
            computed: Tuple[str, ...] = ()
    ):
        return pydantic_model_creator(cls, exclude=exclude, include=include, computed=computed)

    @classmethod
    def QuerySetCreator(
            cls,
            exclude: Tuple[str, ...] = (),
            include: Tuple[str, ...] = (),
            computed: Tuple[str, ...] = ()
    ):
        return pydantic_queryset_creator(cls, exclude=exclude, include=include, computed=computed)

    @property
    def created_time(self) -> str:
        created_at = getattr(self, 'created_at')
        return created_at.strftime('%Y-%m-%d %H:%M:%S') if created_at else ''

    @property
    def updated_time(self) -> str:
        updated_at = getattr(self, 'updated_at')
        return updated_at.strftime('%Y-%m-%d %H:%M:%S') if updated_at else ''

    @classmethod
    def paginate(cls, query, page: int = 1, pagesize: int = 10):
        return query.offset(page - 1).limit(pagesize)

    def to_dict(self, selects: tuple = None, excludes: tuple = None):
        # response dict data of instance serialize

        if not hasattr(self, '_meta'):
            raise AssertionError('<%r> does not have attribute for _meta' % self)
        elif selects:
            return {i: getattr(self, i) for i in selects}
        elif excludes:
            return {i: getattr(self, i) for i in self._meta.fields if i not in excludes}
        else:
            return {i: getattr(self, i) for i in self._meta.fields}
