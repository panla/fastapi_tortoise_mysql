# aerich

[Aerich](https://github.com/tortoise/aerich)
[文档参考](https://tortoise-orm.readthedocs.io/en/latest/migration.html)

## command

```bash
# 初始化，指定配置文件
aerich init -t config.TORTOISE_ORM --location ./migrations

# init db
aerich init-db

# 自动生成sql语句
aerich migrate --name init
aerich migrate --name alter_books_add_column_sn

# 执行到最新的迁移
aerich upgrade
```
