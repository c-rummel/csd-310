from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.csihw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://admin:admin@cluster0.csihw.mongodb.net/?retryWrites=true&w=majority")
db = client.pytech
print(db.list_collection_names())