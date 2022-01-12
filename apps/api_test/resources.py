from fastapi import APIRouter

from extensions import Route, ErrorSchema, resp_success

router = APIRouter(route_class=Route, responses=ErrorSchema)
