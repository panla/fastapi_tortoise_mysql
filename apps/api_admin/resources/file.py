from typing import Optional, List

from fastapi import APIRouter, UploadFile, File

from extensions import Route, resp_success
from conf.define import error_schema
from apps.api_admin.entities import FileSchema

router = APIRouter(route_class=Route, responses=error_schema)


@router.post('', response_model=FileSchema)
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
    return resp_success(data={'file': file_dic, 'files': files_dic})
