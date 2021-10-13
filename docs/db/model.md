# model

## meta

```python
from tortoise import Model, fields


class Car(Model):

    brand = fields.CharField(max_length=100, null=False, index=True, description='品牌')

    class Meta:
        app = 'models'
        table = 'cars'
        table_description = '汽车表'
        unique_together = (('column_a', 'column_b'), )
        indexes = ('column_a', 'column_b')
        # indexes = (('column_a', 'column_b'), ('column_c', 'column_d'))
        ordering = ['name', '-id']
        # 分组查询，annotate 默认排序设置不生效
```