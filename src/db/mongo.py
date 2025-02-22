import os
import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

def create_client(mongo_uri: str):
    try:
        return AsyncIOMotorClient(
            mongo_uri,
            server_api=ServerApi("1"),
            # tlsCAFile=certifi.where(),
            timeoutMS=60000,  # 60 seconds
            uuidRepresentation="standard",
        )
    except Exception as e:
        raise Exception(f"Failed to create MongoDB client: {str(e)}")

class Database:
    _client = None

    @classmethod
    def init(cls, mongo_uri: str):
        try:
            if cls._client is None:
                cls._client = create_client(mongo_uri)
                print("MongoDB client initialized")
        except Exception as e:
            raise Exception(f"Failed to initialize database: {str(e)}")

    @classmethod
    def get_database(cls, db_name: str):
        try:
            if cls._client is None:
                raise Exception("Database client is not initialized")
            return cls._client[db_name]
        except Exception as e:
            raise Exception(f"Failed to get database {db_name}: {str(e)}")

    @classmethod
    def close_client(cls):
        try:
            if cls._client:
                cls._client.close()
                cls._client = None
                print("MongoDB client closed")
        except Exception as e:
            raise Exception(f"Failed to close MongoDB client: {str(e)}")