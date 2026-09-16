from fastapi import APIRouter
from Controller.studentcontroller import CreateStudent
from Model.studentmodel import StudentStruct
from Database.studentdatabase import collection
from Model.updatemodel import UpdateStruct
# from Model.studentUpdate import updateStruct
# from DataBase.dbconnection import collection


router= APIRouter()

@router.post("/createStudent")
def CreateStudent(student:StudentStruct):
    sroll=student.roll
    sname=student.name
    sage=student.age


    sinfo={
          "roll":sroll,
          "name":sname,
          "age":sage
         }

    collection.insert_one(sinfo)

    return {"message":"student created"}

def create(student:StudentStruct):
    return CreateStudent(student)

@router.put("/edit/{roll}")
def UpdateStudent(roll:int,student:UpdateStruct):
    alldata = list(collection.find({},{"_id":0}))

    UpdateStudent = {}


    for i in alldata:
        if i["roll"]==roll:

            if student.name != None:
                UpdateStudent["name"]=student.name

            if student.age != None:
                UpdateStudent["age"]=student.age

            collection.update_one(
                {"roll":roll},
                {"$set":UpdateStudent}
            )

            return{"message": "student updated"}


@router.delete("/delet/{roll}")
def Deletstudent(roll:int):
    alldata= list(collection.find({},{"_id":0}))

    for i in alldata:
        if i["roll"]==roll:
            collection.delete_one({"roll":roll})
            return{"message":"student deleted "}