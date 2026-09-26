from fastapi import APIRouter, HTTPException, status
from pymongo.errors import PyMongoError

from Database.studentdatabase import get_collection
from Model.studentmodel import StudentStruct
from Model.updatemodel import UpdateStruct

router = APIRouter()


def _get_collection():
    try:
        return get_collection()
    except RuntimeError as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database is not configured",
        ) from error
    except PyMongoError as error:
        raise _database_unavailable(error) from error


def _database_unavailable(error: PyMongoError) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Database is unavailable",
    )


@router.post("/createStudent")
def create_student(student: StudentStruct):
    collection = _get_collection()
    try:
        if collection.find_one({"roll": student.roll}, {"_id": 1}):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Student already exists",
            )

        collection.insert_one(student.model_dump())
    except PyMongoError as error:
        raise _database_unavailable(error) from error
    return {"message": "Student created successfully"}


@router.get("/studentslist")
@router.get("/allstudents")
def get_students():
    collection = _get_collection()
    try:
        return list(collection.find({}, {"_id": 0}).sort("roll", 1))
    except PyMongoError as error:
        raise _database_unavailable(error) from error


@router.put("/edit/{roll}")
@router.put("/update/{roll}")
def update_student(roll: int, student: UpdateStruct):
    if roll <= 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Roll must be positive")

    update_data = student.model_dump(exclude_none=True)
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="At least one field is required")

    collection = _get_collection()
    try:
        result = collection.update_one({"roll": roll}, {"$set": update_data})
    except PyMongoError as error:
        raise _database_unavailable(error) from error
    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    return {"message": "Student updated successfully"}


@router.delete("/delet/{roll}")
@router.delete("/delete/{roll}")
def delete_student(roll: int):
    if roll <= 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Roll must be positive")

    collection = _get_collection()
    try:
        result = collection.delete_one({"roll": roll})
    except PyMongoError as error:
        raise _database_unavailable(error) from error
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    return {"message": "Student deleted successfully"}