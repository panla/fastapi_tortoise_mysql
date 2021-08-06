from typing import Optional
from typing import List

from pydantic import BaseModel
from pydantic.fields import Field

from apps.mixins import SchemaMixin


class FileBaseField(BaseModel):
    filename: Optional[str] = Field(default=None, title='file name')


class FileField(BaseModel):
    file: Optional[FileBaseField]
    files: Optional[List[FileBaseField]]


class FileSchema(SchemaMixin):
    """the response schema of upload file"""

    data: Optional[FileField]
