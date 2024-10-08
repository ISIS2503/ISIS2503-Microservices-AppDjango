"""
This module contains the logic for the places app.
Main functions:
- get_places: Get a list of all places
- get_place: Get a single place
- create_place: Create a new place
- update_place: Update a place
- delete_place: Delete a place
"""

from models.models import Place, PlaceCollection
from models.db import places_collection
from bson import ObjectId
from fastapi import HTTPException

def validate_id(place_id: str):
    try:
        ObjectId(place_id)
    except:
        raise HTTPException(status_code=404, detail=f"Place with ID {place_id} not found")

async def get_places():
    """
    Get a list of places
    :return: A list of places
    """
    places = await places_collection.find().to_list(1000)
    return PlaceCollection(places=places)

async def get_place(place_id: str):
    """
    Get a single place
    :param place_id: The ID of the place
    :return: The place
    """
    place_id = validate_id(place_id)
    if (
        place := await places_collection.find_one({"_id": place_id})
    ) is not None:
        return place

    raise HTTPException(status_code=404, detail=f"Place with ID {place_id} not found")

async def create_place(place: Place):
    """
    Insert a new place record.
    """
    new_place = await places_collection.insert_one(
        place.model_dump(by_alias=True, exclude=["id"])
    )
    created_place = await places_collection.find_one(
        {"_id": new_place.inserted_id}
    )
    return created_place

async def update_place(place_id: str, place: Place):
    """
    Update a place
    :param place_id: The ID of the place
    :param place: The place data
    :return: The updated
    """
    place_id = validate_id(place_id)
    
    update_result = await places_collection.update_one(
        {"_id": place_id}, {"$set": place.model_dump(by_alias=True, exclude=["id"])}
    )
    if update_result.modified_count == 1:
        if (
            updated_place := await places_collection.find_one(
                {"_id": place_id}
            )
        ) is not None:
            return updated_place
        
    raise HTTPException(status_code=404, detail=f"Place with ID {place_id} not found")

async def delete_place(place_id: str):
    """
    Delete a place
    :param place_id: The ID of the place
    """
    place_id = validate_id(place_id)
    delete_result = await places_collection.delete_one({"_id": place_id})
    
    if delete_result.deleted_count == 1:
        return
    
    raise HTTPException(status_code=404, detail=f"Place with ID {place_id} not found")