import random
from typing import List, Optional

from app.config import PROBABILITY_GRIMOIRE, PROBABILITY_TYPE_MAGICIAN, TYPES_GRIMOIRES
from app.db import exec_query, insert, select
from app.schemas.grimoire import CreateGrimoire, Grimoire
from fastapi import HTTPException, status


def select_grimoire(type_magician: str) -> Grimoire:
    """
    Select a grimoire based on the type of magician

    Args:
        type_magician (str): Type of magician

    Returns:
        str: Name of grimoire
    """
    probability_magician = list(
        filter(lambda x: x["type"] == type_magician, PROBABILITY_TYPE_MAGICIAN)
    )
    total = sum(PROBABILITY_GRIMOIRE) + probability_magician[0]["probability"]
    rand = random.uniform(0, total)
    upto = 0
    for grimoire in TYPES_GRIMOIRES:
        if upto + grimoire["rarity"] >= rand:
            return save_grimoire(CreateGrimoire(**grimoire, estado="ocupado"))
        upto += grimoire["rarity"]

    return save_grimoire(
        CreateGrimoire(
            **TYPES_GRIMOIRES[0],
        )
    )


def save_grimoire(grimoire: CreateGrimoire) -> Grimoire:
    """
    Save grimoire in database

    Args:
        grimoire (CreateGrimoire): Grimoire model

    Returns:
        Grimoire: Grimoire model
    """
    query, _ = insert(table_name="grimoires", schema="magic_school")  # type: ignore

    row_id = exec_query(query.values(**grimoire.model_dump()))
    return Grimoire(**row_id)  # type: ignore


def get_grimoire(grimoire_id: Optional[int] = None) -> List[Grimoire] | Grimoire:
    """
    Get grimoire by id

    Args:
        grimoire_id (int): Grimoire id

    Returns:
        Grimoire: Grimoire model
    """
    query, table = select(
        table_name="grimoires",  # type: ignore
        columns=[
            "id",
            "nombre",
            "autor",
            "idioma",
            "estado",
            "created_at",
        ],
        schema="magic_school",
    )

    if grimoire_id:
        query = query.where(table.c.id == grimoire_id)

    grimoire_requests = exec_query(query)
    if not grimoire_requests:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Grimoire requests not found"
        )

    return grimoire_requests  # type: ignore
