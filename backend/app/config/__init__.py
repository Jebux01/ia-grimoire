"""
Module to settings
"""

import os
from pydantic_settings import BaseSettings

TYPES_GRIMOIRES = [
    {
        "nombre": "Grimorio de una hoja",
        "autor": "Desconocido",
        "idioma": "Latín",
        "tipo": "comun",
        "rarity": 50,
    },
    {
        "nombre": "Grimorio de dos hojas",
        "autor": "Desconocido",
        "idioma": "Griego",
        "tipo": "comun",
        "rarity": 30,
    },
    {
        "nombre": "Grimorio de tres hojas",
        "autor": "Merlín",
        "idioma": "Inglés antiguo",
        "tipo": "poco habitual",
        "rarity": 15,
    },
    {
        "nombre": "Grimorio de cuatro hojas",
        "autor": "Salomón",
        "idioma": "Hebreo",
        "tipo": "inusual",
        "rarity": 4,
    },
    {
        "nombre": "Grimorio de cinco hojas",
        "autor": "Anónimo",
        "idioma": "Desconocido",
        "tipo": "muy raro",
        "rarity": 1,
    },
]

PROBABILITY_GRIMOIRE = [grimoire["rarity"] for grimoire in TYPES_GRIMOIRES]
PROBABILITY_TYPE_MAGICIAN = [
    {"type": "Oscuro", "probability": 5},
    {"type": "Luz", "probability": 5},
    {"type": "Fuego", "probability": 90},
    {"type": "Agua", "probability": 90},
    {"type": "Viento", "probability": 90},
    {"type": "Tierra", "probability": 90},
]


class Settings(BaseSettings):
    """
    Configurations generals for connections and JWT
    """

    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_SCHEMA: str = os.getenv("DB_SCHEMA", "dbo")
    DB_HOST: str = os.getenv("DB_HOST", "")

    JWT_SECRET_KEY: str = (
        "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    )
    REFRESH_TOKEN_EXPIRES_IN: int = 30
    ACCESS_TOKEN_EXPIRES_IN: int = 30
    JWT_ALGORITHM: str = "HS256"


settings = Settings()
