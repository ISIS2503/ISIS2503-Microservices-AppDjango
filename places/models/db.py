import os
import motor.motor_asyncio
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

# docker run --name mongodb -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=user -e MONGO_INITDB_ROOT_PASSWORD=pass mongodb/mongodb-community-server:$MONGODB_VERSION

# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://monitoring_user:isis2503@localhost:27017?retryWrites=true&w=majority")
db = client.get_database("monitoring_db")
places_collection = db.get_collection("places")

# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]
