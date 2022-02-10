from typing import Optional, List

from pydantic import BaseModel, Field

from extensions import SchemaMixin


class FileField(BaseModel):
    filename: Optional[str] = Field(default=None, title='file name')


class FileEntity(BaseModel):
    file: Optional[FileField]
    files: Optional[List[FileField]]


class FileSchema(SchemaMixin):
    """the response schema of upload file"""

    data: Optional[FileEntity]
