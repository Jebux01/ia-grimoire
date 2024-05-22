"""Module with the endpoint for Auth section"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.config import settings
from app.db import select, exec_query
from app.schemas.magicians import MagicianTokenData
from app.utils.oauth import (
    create_access_token,
    verify_password,
    get_current_active_user,
)

router = APIRouter()


ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN


class ExceptionLogin(Exception):
    """Custom Exception"""


@router.post("/login", status_code=status.HTTP_200_OK)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """Login function"""
    query, table = select(
        table_name="magicians",  # type: ignore
        columns=[
            "nombre",
            "identificacion",
        ],
        schema="magic_school",
    )

    query = query.where(table.c.nombre == form_data.username)

    user_db = exec_query(query)

    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    if not verify_password(
        plain_password=form_data.password,
        hashed_password=user_db["identificacion"],  # type: ignore
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
        )

    access_token: str = create_access_token(MagicianTokenData(**user_db).model_dump())  # type: ignore

    return {
        "status": "success",
        "access_token": access_token,
    }


@router.get("/users/me/")
async def read_users_me(
    current_user: Annotated[MagicianTokenData, Depends(get_current_active_user)]
):
    return current_user
