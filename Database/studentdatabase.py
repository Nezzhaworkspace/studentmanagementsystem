import os

from pymongo import MongoClient
from pymongo.collection import Collection

_connection: MongoClient | None = None
_connection_settings: tuple[str, str, str] | None = None


def get_collection() -> Collection:
	global _connection, _connection_settings

	mongodb_uri = os.getenv("MONGODB_URI")
	if not mongodb_uri:
		raise RuntimeError("MONGODB_URI environment variable is required")

	settings = (
		mongodb_uri,
		os.getenv("MONGODB_DATABASE", "StudentManagement"),
		os.getenv("MONGODB_COLLECTION", "STDCollection1"),
	)
	if _connection is None or _connection_settings != settings:
		_connection = MongoClient(mongodb_uri, serverSelectionTimeoutMS=5000)
		_connection_settings = settings

	return _connection[settings[1]][settings[2]]