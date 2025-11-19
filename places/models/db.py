import os
import motor.motor_asyncio
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

client = motor.motor_asyncio.AsyncIOMotorClient(
    f"mongodb://monitoring_user:isis2503@{os.getenv('PLACES_DB_HOST', '10.128.0.86')}:27017?retryWrites=true&w=majority"
)
db = client.get_database("monitoring_db")
places_collection = db.get_collection("places")


async def set_places_db():
    # Creates a unique index on the code field
    await places_collection.create_index("code", unique=True)


# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]
