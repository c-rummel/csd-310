'''
Caleb Rummel
June 25, 2022
CSD 310 - Module 6 Pytech Update
'''

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.csihw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students = client.pytech.get_collection("students")

docs = students.find({})

print ("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")

for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

print()
print ("-- INSERT STATEMENTS --")

student = {
    "student_id": 1010,
    "first_name": "Jimmy",
    "last_name": "John"
    }
new_student_id = students.insert_one(student).inserted_id
print("Inserted student record {} {} into the students collection with document_id {}".format(student["first_name"], student["last_name"], student["_id"]))

print()
print ("-- DISPLAYING NEW STUDENT LIST DOC --")
docs = students.find({})
for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

doc = students.delete_one({"student_id" : 1010})

print()
print("-- DELETED STUDENT ID: 1010 --")
docs = students.find({})
for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
