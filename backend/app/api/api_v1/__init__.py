"""Module that container all routers base"""

from typing import Dict
from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, magicians, requests_magicians, grimoire

api_router = APIRouter()

NOT_FOUND: Dict = {404: {"description": "Not found"}}

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"],
    responses=NOT_FOUND,
)

api_router.include_router(
    requests_magicians.router,
    prefix="",
    tags=["Solicitudes"],
    responses=NOT_FOUND,
)


api_router.include_router(
    grimoire.router,
    prefix="/grimoire",
    tags=["Grimorios"],
    responses=NOT_FOUND,
)


api_router.include_router(
    magicians.router,
    prefix="/magicians",
    tags=["Magos"],
    responses=NOT_FOUND,
)
