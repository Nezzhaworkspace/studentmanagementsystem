from Model.studentmodel import StudentStruct
from Database.studentdatabase import collection

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

def GetStudent():
    alldata = list(collection.find({},{"_id":0}))
    return alldata

