"""
Module with the model of business logic for the Magicians section
"""

from typing import Any, Callable, Dict, List, Mapping, Optional

from fastapi import HTTPException, status
from sqlalchemy import and_

from app.db import exec_query, insert, select, update
from app.model.grimoire import select_grimoire
from app.model.magicians import create_magician
from app.schemas.magicians import CreateMagician
from app.schemas.requests import (
    CreateRequests,
    Requests,
    UpdateRequest,
    UpdateRequestStatus,
)


STATES_ACCEPTED = ("aceptada", "rechazada", "pendiente", "revision")
NOW_STR = "now()"


def create_request(requests_magic: CreateRequests) -> Dict[str, str | Mapping]:
    """
    Create a new requests

    Args:
        requests_magic: CreateRequests model

    Returns:
        Dict: Response message
    """
    query, _ = insert(table_name="requests", schema="magic_school")  # type: ignore

    row_id = exec_query(query.values(**requests_magic.model_dump()))
    return {"status": "success", "message": "Solicitud creada", "data": row_id}  # type: ignore


def get_requests(request_id: Optional[int] = None) -> List[Requests] | Requests:
    """
    Get all requests

    Args:
        request_id: Request id

    Returns:
        Any: Requests model
    """
    query, table = select(
        table_name="requests",  # type: ignore
        columns=[
            "id",
            "nombre",
            "apellido",
            "identificacion",
            "edad",
            "afinidad_magica",
            "estado_solicitud",
        ],
        schema="magic_school",
    )

    if request_id:
        query = query.where(table.c.id == request_id)

    magicians = exec_query(query.order_by(table.c.id.desc(), table.c.created_at.desc()))

    if not magicians:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Magicians not found"
        )

    return magicians  # type: ignore


def update_request(
    requests_id: int,
    requests_magic: UpdateRequest,
) -> Dict[str, str]:
    """
    Update a requests

    Args:
        requests_id: Request id
        requests_magic: UpdateRequest model

    Returns:
        Dict: Response message
    """
    query, table = update(
        table_name="requests",  # type: ignore
        schema="magic_school",
    )

    requests_magic.update_at = NOW_STR
    query = query.where(table.c.id == requests_id).values(**requests_magic.model_dump())

    exec_query(query)
    return {
        "status": "success",
        "message": f"Solicitud actualizada con id: {requests_id}",
    }


def update_partial_request_status(
    requests_id: int,
    status: UpdateRequestStatus,
) -> Dict[str, str | Mapping]:
    """
    Update magician status

    Args:
        requests_id: Request id
        status: UpdateRequestStatus model

    Returns:
        Dict: Response message
    """

    process = eval_state_request(status.estado_solicitud)

    query, table = update(
        table_name="requests",  # type: ignore
        schema="magic_school",
    )

    status.update_at = NOW_STR
    query = query.where(table.c.id == requests_id).values(**status.model_dump())

    update_result = exec_query(query)
    if not update_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Solictud no encontrada"  # type: ignore
        )

    if isinstance(process, Callable):
        result_accept = process(requests_id)
        return result_accept

    return {
        "status": "success",
        "message": "Estado de la solicitud actualizada",
    }


def eval_state_request(state: str) -> str | Callable:
    """Evaluate the state of the request"""
    if state not in STATES_ACCEPTED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Estado no valido"  # type: ignore
        )

    if state == "aceptada":
        return acceptance_process

    return "next"


def acceptance_process(requests_id: int) -> Dict[str, str | Mapping]:
    """Accept a requests"""
    request: Requests | List[Requests] = get_requests(request_id=requests_id)
    grimoire = select_grimoire(request.afinidad_magica)  # type: ignore
    magician: CreateMagician = CreateMagician(**request, grimorio_id=grimoire.id)  # type: ignore
    magician_created = create_magician(magician)
    return {
        "status": "success",
        "message": f"Solicitud aceptada con id: {requests_id}",
        "data": magician_created,
    }


def delete_request(requests_id: int) -> Dict[str, str]:
    """Delete a requests"""
    query, table = update(
        table_name="requests",  # type: ignore
        schema="magic_school",
    )

    query = query.where(table.c.id == requests_id).values(
        estado_solicitud="rechazada", deleted_at=NOW_STR
    )

    exec_query(query)
    return {
        "status": "success",
        "message": f"Solicitud eliminada con id: {requests_id}",
    }
