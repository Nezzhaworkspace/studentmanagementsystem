from Database.studentdatabase import get_collection
from Model.studentmodel import StudentStruct


def CreateStudent(student: StudentStruct):
    collection = get_collection()
    sinfo = student.model_dump()

    if collection.find_one({"roll": student.roll}, {"_id": 1}):
        return {"message": "Student already exists"}

    collection.insert_one(sinfo)
    return {"message": "student created"}


def GetStudent():
    collection = get_collection()
    return list(collection.find({}, {"_id": 0}).sort("roll", 1))

