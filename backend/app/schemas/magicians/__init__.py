"""
Schemas for magicians
"""

from pydantic import BaseModel


class MagicianLogin(BaseModel):
    """Base model for Login user"""

    nombre: str
    identificacion: str


class MagicianTokenData(BaseModel):
    """Data untoken"""

    nombre: str
    identificacion: str


class Magician(BaseModel):
    """Base model for Magician"""

    id: int
    nombre: str
    apellido: str
    identificacion: str
    edad: int
    afinidad_magica: str
    grimoire: str


class CreateMagician(BaseModel):
    """Base model for create Magician"""

    nombre: str
    apellido: str
    identificacion: str
    edad: int
    afinidad_magica: str
    grimorio_id: int


class CreatedMagician(CreateMagician):
    """Base model for create Magician"""

    id: int