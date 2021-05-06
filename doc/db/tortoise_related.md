# `prefetch_related`

## code

```text
from tortoise import fields, Model
from tortoise.queryset import Prefetch


class Cup(Model, ModelMixin):
    id = fields.BigIntField(pk=True, description='主键')
    owner = fields.ForeignKeyField('models.User', related_name='cups', db_constraint=False)
    # owner_id = fields.BigIntField()
    price = fields.IntField()

    @property
    def created_time(self) -> str:
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    @property
    def updated_time(self) -> str:
        return self.updated_at.strftime('%Y-%m-%d %H:%M:%S')


instance = await Cup.all().prefetch_related(Prefetch('owner', queryset=User.filter(cellphone__icontains='188'))).first()

此时 instance 包含了 owner 对象，可以直接在 Pydantic BaseModel 中调用

可以直接使用非异步的属性方法
可以通过 prefetch_related(Prefetch()) 来 join 查询
    但是需要 一对多，多对多，一对一 关系
    可以是只有关系，没有实际约束 db_constraint=False

不支持异步属性方法
```
