import motor.motor_asyncio
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://monitoring_user:isis2503@10.128.0.87:27017?retryWrites=true&w=majority")
db = client.get_database("monitoring_db")
places_collection = db.get_collection("places")

# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]
