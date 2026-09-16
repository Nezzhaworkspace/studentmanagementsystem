from pymongo import MongoClient

ConnectionString = MongoClient ("mongodb+srv://nehabombe2001_db_user:C6nznpO7vh4z4pmG@cluster0.whabr5c.mongodb.net/?appName=Cluster0")
database = ConnectionString["StudentManagement"]

collection = database["STDCollection1"]     

#jj9ymatIoEg9NwlB
#mongodb+srv://nehabombe2001_db_user:<db_password>jj9ymatIoEg9NwlB@cluster0.whabr5c.mongodb.net/?appName=Cluster0
# mongodb+srv://nehabombe2001_db_user:<db_password>@cluster0.whabr5c.mongodb.net/?appName=Cluster0
# C6nznpO7vh4z4pmG