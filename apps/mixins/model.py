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


class ModelMixin(object):

    @classmethod
    def ModelCreator(cls, exclude: Tuple[str, ...] = (), include: Tuple[str, ...] = ()):
        return pydantic_model_creator(cls, exclude=exclude, include=include)

    @classmethod
    def QuerySetCreator(cls, exclude: Tuple[str, ...] = (), include: Tuple[str, ...] = ()):
        return pydantic_queryset_creator(cls, exclude=exclude, include=include)
