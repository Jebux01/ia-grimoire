"""
Grimoire endpoints
"""

from fastapi import APIRouter, status

from app.model.grimoire import get_grimoire

router = APIRouter()


@router.get("/grimorios", status_code=status.HTTP_200_OK)
def get_grimoire_requests():
    """Get all grimoire requests"""
    return get_grimoire()


@router.get("/grimorios/{grimoire_id}", status_code=status.HTTP_200_OK)
def get_grimoire_request(grimoire_id: int):
    """Get grimoire request by id"""
    return get_grimoire(grimoire_id)
