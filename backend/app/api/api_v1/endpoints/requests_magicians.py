"""Module with the endpoints for Magicians section"""

from typing import List, Dict, Mapping
from fastapi import APIRouter, HTTPException, requests, status
from app.model.requests import (
    create_request,
    delete_request,
    get_requests,
    update_request,
    update_partial_request_status,
)

from app.schemas.requests import (
    CreateRequests,
    Requests,
    UpdateRequest,
    UpdateRequestStatus,
)

router = APIRouter()


@router.get("/solicitudes", status_code=status.HTTP_200_OK)
def get_requests_endpoint() -> List[Requests]:
    """Get all requests"""
    result = get_requests()

    if isinstance(result, Mapping):
        return [Requests(**result)]  # type: ignore

    return result  # type: ignore


@router.get("/solicitudes/{requests_id}", status_code=status.HTTP_200_OK)
def get_requests_endpoint_by(requests_id: int) -> Requests:
    """Get request by id"""
    return Requests(**get_requests(request_id=requests_id))  # type: ignore


@router.post("/solicitudes", status_code=status.HTTP_201_CREATED)
def create_request_endpoint(requests_magic: CreateRequests) -> Dict[str, str | Mapping]:
    """Create a new requests"""
    result = create_request(requests_magic)
    return result


@router.put("/solicitudes/{requests_id}", status_code=status.HTTP_200_OK)
def update_request_endpoint(
    requests_id: int, requests_magic: UpdateRequest
) -> Dict[str, str]:
    """Update a requests"""
    return update_request(requests_id, requests_magic)


@router.patch("/solicitudes/{requests_id}/estatus", status_code=status.HTTP_200_OK)
def update_requests_status(
    requests_id: int, status: UpdateRequestStatus
) -> Dict[str, str | Mapping]:
    """Update a requests status"""
    return update_partial_request_status(requests_id, status)


@router.delete("/solicitud/{requests_id}", status_code=status.HTTP_200_OK)
def delete_request_endpoint(requests_id: int) -> Dict[str, str]:
    """Delete a magician"""
    return delete_request(requests_id)
