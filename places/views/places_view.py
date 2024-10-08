from fastapi import APIRouter, status, Body
import logic.places_logic as places_service
from models.models import Place, PlaceCollection

router = APIRouter()
ENDPOINT_NAME = "/places"


@router.get(
    "/",
    response_description="List all places",
    response_model=PlaceCollection,
    status_code=status.HTTP_200_OK,
)
async def get_places():
    return await places_service.get_places()


@router.get(
    "/{place_id}",
    response_description="Get a single place",
    response_model=Place,
    status_code=status.HTTP_200_OK,
)
async def get_place(place_id: str):
    return await places_service.get_place(place_id)


@router.post(
    "/",
    response_description="Create a new place",
    response_model=Place,
    status_code=status.HTTP_201_CREATED,
)
async def create_place(place: Place = Body(...)):
    return await places_service.create_place(place)


@router.put(
    "/{place_id}",
    response_description="Update a place",
    response_model=Place,
    status_code=status.HTTP_200_OK,
)
async def update_place(place_id: str, place: Place = Body(...)):
    return await places_service.update_place(place_id, place)


@router.delete(
    "/{place_id}",
    response_description="Delete a place",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_place(place_id: str):
    return await places_service.delete_place(place_id)
