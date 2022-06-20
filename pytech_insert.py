"""
Caleb Rummel
June 19, 2022
CSD 310 - Assignment 5.3
"""

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.csihw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students = client.pytech.get_collection("students")

student = {
    "student_id": 1007,
    "first_name": "John",
    "last_name": "Smith"
    }
new_student_id = students.insert_one(student).inserted_id
print("Inserted student record {} {} into the students collection with document_id {}".format(student["first_name"], student["last_name"], student["_id"]))

student = {
    "student_id": 1008,
    "first_name": "Jane",
    "last_name": "Porter"
    }
new_student_id = students.insert_one(student).inserted_id
print("Inserted student record {} {} into the students collection with document_id {}".format(student["first_name"], student["last_name"], student["_id"]))

student = {
    "student_id": 1009,
    "first_name": "Jimmy",
    "last_name": "Neutron"
    }
new_student_id = students.insert_one(student).inserted_id
print("Inserted student record {} {} into the students collection with document_id {}".format(student["first_name"], student["last_name"], student["_id"]))