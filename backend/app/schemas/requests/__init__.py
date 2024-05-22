import enum
import re

from pydantic import BaseModel, validator, field_validator
from typing import Optional

from app.db import update


class MagicalAffinity(str, enum.Enum):
    """Base model for Magical Affinity"""

    OSCURIDAD = "Oscuro"
    LUZ = "Luz"
    FUEGO = "Fuego"
    AGUA = "Agua"
    VIENTO = "Viento"
    TIERRA = "Tierra"


class Requests(BaseModel):
    """Base model for user"""

    id: int
    nombre: str
    apellido: str
    identificacion: str
    edad: int
    estado_solicitud: str
    afinidad_magica: MagicalAffinity


class CreateRequests(BaseModel):
    """Base model for create user"""

    nombre: str
    apellido: str
    identificacion: str
    edad: int
    afinidad_magica: MagicalAffinity

    @field_validator("nombre", "apellido", mode="wrap")
    def validate_nombre(cls, value, _, ctx):
        """Validate nombre and apellido"""
        if not re.match("^[a-zA-Z]{1,10}$", value):
            raise ValueError(
                f"El campo {ctx.field_name} no cumple con el formato (solo letras y maximo 10 caracteres)"
            )

        return value

    @validator("identificacion")
    def validate_identificacion(cls, value):
        """Validate identificacion"""

        if not re.match("^[a-zA-Z0-9]{1,10}$", value):
            raise ValueError(
                "Identificacion no puede tener caracteres especiales ni espacios y maximo 10 caracteres"
            )

        return value

    @validator("edad")
    def validate_edad(cls, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Edad debe ser un numero")

        """Validate edad"""
        if value < 0:
            raise ValueError("Edad no puede ser negativa")

        if len(str(value)) >= 3:
            raise ValueError("Edad no puede tener mas de 3 digitos")

        return value

    @validator("afinidad_magica")
    def validate_afinidad_magica(cls, value):
        """Validate afinidad_magica"""
        if value not in MagicalAffinity:
            raise ValueError("Afinidad magica no es valida")

        return value.value


class UpdateRequest(CreateRequests):
    estado_solicitud: str
    update_at: Optional[str] = None


class UpdateRequestStatus(BaseModel):
    """Base model for update user status"""

    estado_solicitud: str
    update_at: Optional[str] = None
