from typing import Optional
from pydantic import BaseModel


class Grimoire(BaseModel):
    """Base model for Grimoire"""

    id: int
    nombre: str
    autor: str
    idioma: str
    estado: Optional[str]
    tipo: str


class CreateGrimoire(BaseModel):
    """Base model for create Grimoire"""

    nombre: str
    autor: str
    idioma: str
    estado: Optional[str]
    tipo: str
