from fastapi import APIRouter

from views import places_view

VERSION_PREFIX = "/v1"
router = APIRouter()

router.include_router(places_view.router, prefix=places_view.ENDPOINT_NAME)