__all__ = [
    'UnsignedTinyIntField', 'UnsignedSmallIntField', 'UnsignedIntField', 'UnsignedBigIntField',
]

from typing import Any

from tortoise.fields.base import Field


class UnsignedTinyIntField(Field, int):
    SQL_TYPE = "TINYINT UNSIGNED"
    allows_generated = True

    def __init__(self, pk: bool = False, **kwargs: Any) -> None:
        if pk:
            kwargs["generated"] = bool(kwargs.get("generated", True))
        super().__init__(pk=pk, **kwargs)

    @property
    def constraints(self) -> dict:
        return {
            "ge": 1 if self.generated or self.reference else 0,
            "le": 255,
        }

    class _db_mysql:
        GENERATED_SQL = "TINYINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT"


class UnsignedSmallIntField(Field, int):
    SQL_TYPE = "SMALLINT UNSIGNED"
    allows_generated = True

    def __init__(self, pk: bool = False, **kwargs: Any) -> None:
        if pk:
            kwargs["generated"] = bool(kwargs.get("generated", True))
        super().__init__(pk=pk, **kwargs)

    @property
    def constraints(self) -> dict:
        return {
            "ge": 1 if self.generated or self.reference else 0,
            "le": 65535,
        }

    class _db_mysql:
        GENERATED_SQL = "SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT"


class UnsignedIntField(Field, int):
    SQL_TYPE = "INT UNSIGNED"
    allows_generated = True

    def __init__(self, pk: bool = False, **kwargs: Any) -> None:
        if pk:
            kwargs["generated"] = bool(kwargs.get("generated", True))
        super().__init__(pk=pk, **kwargs)

    @property
    def constraints(self) -> dict:
        return {
            "ge": 1 if self.generated or self.reference else 0,
            "le": 4294967295,
        }

    class _db_mysql:
        GENERATED_SQL = "INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT"


class UnsignedBigIntField(Field, int):
    SQL_TYPE = "BIGINT UNSIGNED"
    allows_generated = True

    def __init__(self, pk: bool = False, **kwargs: Any) -> None:
        if pk:
            kwargs["generated"] = bool(kwargs.get("generated", True))
        super().__init__(pk=pk, **kwargs)

    @property
    def constraints(self) -> dict:
        return {
            "ge": 1 if self.generated or self.reference else 0,
            "le": 18446744073709551615,
        }

    class _db_mysql:
        GENERATED_SQL = "BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT"
