"""
This file contains the endpoints for the magicians table.
"""

from typing import List, Mapping
from fastapi import APIRouter, status

from app.schemas.magicians import Magician
from app.model.magicians import get_magicians as get_am

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def get_magicians() -> List[Magician]:
    """Get all magicians"""
    result = get_am()
    if isinstance(result, Mapping):
        return [Magician(**result)]  # type: ignore
    return result  # type: ignore


@router.get("/{magician_id}", status_code=status.HTTP_200_OK)
def get_magician(magician_id: int) -> Magician:
    """Get magician by id"""
    result = get_am(magicians_id=magician_id)
    return Magician(**result)  # type: ignore
