"""
Caleb Rummel
June 19, 2022
CSD 310 - Assignment 5.3
"""

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.csihw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students = client.pytech.get_collection("students")

docs = students.find({})

print ("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")

for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

print()
print ("--DISPLAYING STUDENT DOCUMENT FORM find_one() QUERY--")
doc = students.find_one({"student_id": 1007})
print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])