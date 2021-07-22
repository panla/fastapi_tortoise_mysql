from typing import Optional
from typing import List

from pydantic import BaseModel
from pydantic.fields import Field


class FileBaseField(BaseModel):
    filename: Optional[str] = Field(default=None, title='文件名')


class FileField(BaseModel):
    file: Optional[FileBaseField]
    files: Optional[List[FileBaseField]]


class FileSchema(BaseModel):
    """the response schema of upload file"""

    status_code: int = 10000
    message: str = ''
    data: Optional[FileField]
