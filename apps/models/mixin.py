from tortoise import fields
from tortoise.models import Model


class BaseModel(Model):
    id = fields.BigIntField(pk=True, description='主键')
    created_at = fields.DatetimeField(auto_now_add=True, null=False, description='创建时间')
    updated_at = fields.DatetimeField(auto_now=True, null=False, description='更新时间')
    is_delete = fields.BooleanField(null=False, default=False, description='删除标识')

    @property
    def created_time(self) -> str:
        created_at = getattr(self, 'created_at')
        return created_at.strftime('%Y-%m-%d %H:%M:%S') if created_at else ''

    @property
    def updated_time(self) -> str:
        updated_at = getattr(self, 'updated_at')
        return updated_at.strftime('%Y-%m-%d %H:%M:%S') if updated_at else ''

    class Meta:
        abstract = True


class ModelMixin(object):
    __slots__ = ()

    def __init__(self, **kwargs):
        pass

    @staticmethod
    def to_dict(instance, selects: tuple = None, excludes: tuple = None) -> dict:

        if not hasattr(instance, '_meta'):
            raise AssertionError('<%r> does not have attribute for _meta' % instance)

        if selects:
            return {i: getattr(instance, i) for i in selects}
        elif excludes:
            return {i: getattr(instance, i) for i in instance._meta.fields if i not in excludes}
        else:
            return {i: getattr(instance, i) for i in instance._meta.fields}

    async def async_to_dict(self, selects: tuple = None, excludes: tuple = None, second_attrs: dict = None) -> dict:
        """response dict data of instance serialize

        selects: ('id', 'name')
        excludes: ('created_at', 'updated_at')
        second_attrs: {'owner': ['id', 'name'], 'agency': ['id', 'name']}
        """

        results = self.to_dict(self, selects=selects, excludes=excludes)
        if second_attrs:
            for attr, columns in second_attrs.items():
                results.update({attr: self.to_dict(await getattr(self, attr), selects=columns)})

        return results

    def sync_to_dict(self, selects: tuple = None, excludes: tuple = None, second_attrs: dict = None) -> dict:
        """response dict data of instance serialize

        selects: ('id', 'name')
        excludes: ('created_at', 'updated_at')
        second_attrs: {'owner': ['id', 'name'], 'agency': ['id', 'name']}
        """

        results = self.to_dict(self, selects=selects, excludes=excludes)
        if second_attrs:
            for attr, columns in second_attrs.items():
                results.update({attr: self.to_dict(getattr(self, attr), selects=columns)})

        return results
