"""
Num
    8-bit : TinyInt     UnsignedTinyInt
    16-bit: SmallInt    UnsignedSmallInt
    24-bit: MediumInt   UnsignedMediumInt
    32-bit: Int         UnsignedInt
    64-bit: BitInt      UnsignedBitInt

    FloatField: DOUBLE
    DecimalField

EnumField
    IntEnumField    0 <= value < 32768
    CharEnumField
"""
from typing import Any

from tortoise.fields.data import SmallIntField, IntField, BigIntField


class TinyIntField(SmallIntField):
    """
    Tiny integer field. (8-bit unsigned)

    pk (bool):
        True if field is Primary Key.
    """

    SQL_TYPE = "TINYINT"
    allows_generated = True

    def __init__(self, pk: bool = False, **kwargs: Any) -> None:
        if pk:
            kwargs["generated"] = bool(kwargs.get("generated", True))
        super().__init__(pk=pk, **kwargs)

    @property
    def constraints(self) -> dict:
        return {
            "ge": 1 if self.generated or self.reference else -128,
            "le": 127
        }

    class _db_mysql:
        GENERATED_SQL = "TINYINT NOT NULL PRIMARY KEY AUTO_INCREMENT"


class MediumIntField(IntField):
    """
    Medium integer field. (24-bit unsigned)

    pk (bool):
        True if field is Primary Key.
    """

    SQL_TYPE = "MEDIUMINT"
    allows_generated = True

    def __init__(self, pk: bool = False, **kwargs: Any) -> None:
        if pk:
            kwargs["generated"] = bool(kwargs.get("generated", True))
        super().__init__(pk=pk, **kwargs)

    @property
    def constraints(self) -> dict:
        return {
            "ge": 1 if self.generated or self.reference else -8388608,
            "le": 8388607
        }

    class _db_mysql:
        GENERATED_SQL = "MEDIUMINT NOT NULL PRIMARY KEY AUTO_INCREMENT"


class UnsignedTinyIntField(SmallIntField):
    """
    Unsigned Tiny integer field. (8-bit unsigned)

    pk (bool):
        True if field is Primary Key.
    """

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
            "le": 255
        }

    class _db_mysql:
        GENERATED_SQL = "TINYINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT"


class UnsignedSmallIntField(SmallIntField):
    """
    Unsigned Small integer field. (16-bit unsigned)

    pk (bool):
        True if field is Primary Key.
    """

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
            "le": 65535
        }

    class _db_mysql:
        GENERATED_SQL = "SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT"


class UnsignedMediumIntField(IntField):
    """
    Unsigned Medium integer field. (24-bit unsigned)

    pk (bool):
        True if field is Primary Key.
    """

    SQL_TYPE = "MEDIUMINT UNSIGNED"
    allows_generated = True

    def __init__(self, pk: bool = False, **kwargs: Any) -> None:
        if pk:
            kwargs["generated"] = bool(kwargs.get("generated", True))
        super().__init__(pk=pk, **kwargs)

    @property
    def constraints(self) -> dict:
        return {
            "ge": 1 if self.generated or self.reference else 0,
            "le": 16777215
        }

    class _db_mysql:
        GENERATED_SQL = "MEDIUMINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT"


class UnsignedIntField(IntField):
    """
    Unsigned Int integer field. (32-bit unsigned)

    pk (bool):
        True if field is Primary Key.
    """

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
            "le": 4294967295
        }

    class _db_mysql:
        GENERATED_SQL = "INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT"


class UnsignedBigIntField(BigIntField):
    """
    Unsigned Big integer field. (64-bit unsigned)

    pk (bool):
        True if field is Primary Key.
    """

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
            "le": 18446744073709551615
        }

    class _db_mysql:
        GENERATED_SQL = "BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT"
