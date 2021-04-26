from typing import Optional
from typing import List

from fastapi import Body, Query
from pydantic import BaseModel
from pydantic.fields import Field


class FileField(BaseModel):
    filename: Optional[str] = Field(default=None, title='文件名')


class FileSchema(BaseModel):
    """上传文件接口返回参数"""

    file: Optional[FileField]
    files: Optional[List[FileField]]
