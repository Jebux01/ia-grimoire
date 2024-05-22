"""Module that container all routers base"""

from fastapi import APIRouter, status

from app.api.api_v1.endpoints import auth, magicians, requests_magicians, grimoire

api_router = APIRouter()

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

api_router.include_router(
    requests_magicians.router,
    prefix="",
    tags=["Solicitudes"],
    responses={404: {"description": "Not found"}},
)


api_router.include_router(
    grimoire.router,
    prefix="/grimoire",
    tags=["Grimorios"],
    responses={404: {"description": "Not found"}},
)


api_router.include_router(
    magicians.router,
    prefix="/magicians",
    tags=["Magos"],
    responses={404: {"description": "Not found"}},
)
