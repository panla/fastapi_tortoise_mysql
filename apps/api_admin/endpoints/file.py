from typing import Optional, List

from fastapi import APIRouter, UploadFile, File
from starlette.status import HTTP_201_CREATED

from extensions import Route, ErrorSchema
from apps.api_admin.schemas import FileSchema

router = APIRouter(route_class=Route, responses=ErrorSchema)


@router.post('', response_model=FileSchema, status_code=HTTP_201_CREATED)
async def upload_file(
        file: Optional[UploadFile] = File(default=None),
        files: Optional[List[UploadFile]] = File(default=None),
):
    """the api of upload file"""

    file_dic = dict()
    if file:
        filename = file.filename
        file_dic = {'filename': filename}

    files_dic = []
    if files:
        for f in files:
            filename = f.filename
            files_dic.append({'filename': filename})
    return FileSchema(data={'file': file_dic, 'files': files_dic})
