from fastapi import FastAPI

import config

v1_admin_app: FastAPI = FastAPI(include_in_schema=config.include_in_schema)
