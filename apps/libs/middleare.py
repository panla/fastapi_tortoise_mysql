from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



def register_cross(app: FastAPI):
    """解决跨域"""

    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex='https?://.*',
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
