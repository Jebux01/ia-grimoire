"""
OAuth functions

This module contains functions to manage the OAuth2 authentication.
"""

from datetime import datetime, timedelta, UTC  # noqa: F401  # type: ignore
from typing import Annotated, Dict

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import settings
from app.schemas.magicians import Magician, MagicianTokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: Dict):
    """Create token with data send

    Args:
        data (Dict): data to encrypted

    Returns:
        str: JWT Generated
    """
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRES_IN)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Decrypt data from the token

    Args:
        token (str): Token to decrypt

    Returns:
        UserTokenData: User data

    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=settings.JWT_ALGORITHM,
        )

        user: MagicianTokenData = MagicianTokenData(**payload)
        if user is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception from JWTError

    return user


async def get_current_active_user(
    current_user: Annotated[Magician, Depends(get_current_user)]
) -> Magician:
    """
    Check if user is active

    Args:
        current_user (User): User data

    Returns:
        User: User data
    """
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")

    return current_user


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password

    Args:
        plain_password (str): Plain password
        hashed_password (str): Hashed password

    Returns:
        bool: True if password is correct
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Get password hash

    Args:
        password (str): Plain password

    Returns:
        str: Hashed password
    """
    return pwd_context.hash(password)
