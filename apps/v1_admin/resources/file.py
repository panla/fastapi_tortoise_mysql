from typing import Optional, List

from fastapi import APIRouter
from fastapi import UploadFile, File

from apps.extensions import Route
from apps.utils import resp_success, error_response
from apps.v1_admin.entities import FileSchema

router = APIRouter(route_class=Route)


@router.post('', response_model=FileSchema, responses=error_response)
async def upload_file(
        file: Optional[UploadFile] = File(default=None),
        files: Optional[List[UploadFile]] = File(default=None),
):
    """在 /api/v1/admin/docs swagger 上暂未找到上传多张图片的方法"""

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
