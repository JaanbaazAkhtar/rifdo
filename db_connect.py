from pymongo import MongoClient
import pymongo
import gridfs

CONNECTION_STRING = "mongodb+srv://sanaeram5:rifdo#123@cluster0.srkj4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
mydb = client["rifdo"]
studentTable = mydb.table1
st = {
     "rollno":"mca019",
     "name":"Jaanbaaz",
     "img":"C:/Users/Asus/Pictures/Camera Roll/jpic.jpg"
}

studentTable.insert_one(st)


