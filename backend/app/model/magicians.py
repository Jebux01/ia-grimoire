from app.db import exec_query, insert, join, select
from app.schemas.magicians import CreateMagician, Magician, CreatedMagician
from typing import Dict, List, Optional
from fastapi import HTTPException, status


def create_magician(magician: CreateMagician) -> Dict[str, str]:
    """
    Create a new magician

    Args:
        magician: CreateMagician model

    Returns:
        Dict: Response message
    """
    query, _ = insert(table_name="magicians", schema="magic_school")  # type: ignore

    object_created = exec_query(query.values(**magician.model_dump()))
    return CreatedMagician(**object_created).model_dump()  # type: ignore


def get_magicians(magicians_id: Optional[int] = None) -> List[Magician] | Magician:
    """
    Get all magicians

    Returns:
        List: List of magicians
    """
    query, tables = join(
        table_name="magicians m",  # type: ignore
        columns=[
            "m.id",
            "m.nombre",
            "m.apellido",
            "m.identificacion",
            "m.edad",
            "m.afinidad_magica",
            "g.nombre as grimoire",
        ],
        config={
            "tables": [
                {
                    "table": "grimoires g",
                    "onclause": "m.grimorio_id = g.id",
                    "type": "left",
                    "schema": "magic_school",
                }
            ]
        },
        schema="magic_school",
    )

    if magicians_id:
        query = query.where(tables.m.c.id == magicians_id)

    magicians = exec_query(
        query.order_by(tables.m.c.id.desc(), tables.m.c.created_at.desc())
    )

    if not magicians:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Magicians not found"
        )

    return magicians  # type: ignore
