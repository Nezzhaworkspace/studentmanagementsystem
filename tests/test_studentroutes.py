from copy import deepcopy
from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from main import app
from Routes import studentroutes


class FakeCursor:
    def __init__(self, records):
        self.records = records

    def sort(self, field, direction):
        self.records.sort(key=lambda record: record[field], reverse=direction < 0)
        return self

    def __iter__(self):
        return iter(self.records)


class FakeCollection:
    def __init__(self):
        self.records = {}

    def find_one(self, query, projection=None):
        return self.records.get(query["roll"])

    def insert_one(self, record):
        self.records[record["roll"]] = deepcopy(record)

    def find(self, query, projection=None):
        return FakeCursor([deepcopy(record) for record in self.records.values()])

    def update_one(self, query, update):
        record = self.records.get(query["roll"])
        if record is None:
            return SimpleNamespace(matched_count=0)
        record.update(update["$set"])
        return SimpleNamespace(matched_count=1)

    def delete_one(self, query):
        deleted = self.records.pop(query["roll"], None)
        return SimpleNamespace(deleted_count=int(deleted is not None))


@pytest.fixture
def client(monkeypatch):
    collection = FakeCollection()
    monkeypatch.setattr(studentroutes, "get_collection", lambda: collection)
    return TestClient(app), collection


def student_payload(roll=1):
    return {
        "roll": roll,
        "name": "Ada Lovelace",
        "age": 20,
        "email": "ada@example.com",
    }


def test_create_list_update_and_delete_student(client):
    http, collection = client

    created = http.post("/createStudent", json=student_payload())
    assert created.status_code == 200
    assert created.json() == {"message": "Student created successfully"}
    collection.insert_one(student_payload(roll=3))
    collection.insert_one(student_payload(roll=2))

    listed = http.get("/studentslist")
    assert listed.status_code == 200
    assert [student["roll"] for student in listed.json()] == [1, 2, 3]

    updated = http.put("/edit/1", json={"name": "Ada Byron", "age": 21})
    assert updated.status_code == 200
    assert http.get("/studentslist").json()[0]["name"] == "Ada Byron"

    deleted = http.delete("/delet/1")
    assert deleted.status_code == 200
    assert http.delete("/delet/2").status_code == 200
    assert http.delete("/delet/3").status_code == 200
    assert http.get("/studentslist").json() == []


def test_duplicate_and_missing_students_return_conflicts(client):
    http, _ = client
    assert http.post("/createStudent", json=student_payload()).status_code == 200
    assert http.post("/createStudent", json=student_payload()).status_code == 409
    assert http.put("/edit/99", json={"name": "Missing"}).status_code == 404
    assert http.delete("/delet/99").status_code == 404


@pytest.mark.parametrize(
    "payload",
    [
        {**student_payload(), "email": "not-an-email"},
        {**student_payload(), "roll": 0},
        {**student_payload(), "age": 0},
        {**student_payload(), "unexpected": "field"},
    ],
)
def test_create_rejects_invalid_student_data(client, payload):
    http, _ = client
    assert http.post("/createStudent", json=payload).status_code == 422


def test_empty_update_is_rejected(client):
    http, _ = client
    assert http.put("/edit/1", json={}).status_code == 400


def test_database_configuration_error_returns_service_unavailable(monkeypatch):
    def missing_database():
        raise RuntimeError("MONGODB_URI environment variable is required")

    monkeypatch.setattr(studentroutes, "get_collection", missing_database)
    response = TestClient(app).get("/studentslist")
    assert response.status_code == 503
    assert response.json() == {"detail": "Database is not configured"}


def test_database_connection_error_returns_service_unavailable(client):
    http, collection = client

    def database_is_down(*args, **kwargs):
        from pymongo.errors import ServerSelectionTimeoutError

        raise ServerSelectionTimeoutError("database is unreachable")

    collection.find = database_is_down
    response = http.get("/studentslist")
    assert response.status_code == 503
    assert response.json() == {"detail": "Database is unavailable"}