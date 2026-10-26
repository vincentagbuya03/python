import json
import csv
students = [
    {"id" : "23-sc-4111","name": "Vincent Agbuya", "age": 21},
    {"id" : "23-sc-4112","name": "Glend Allyzza Loresco", "age": 22},
    {"id" : "23-sc-4113","name": "Sir Napoleon Hermoso", "age": 32},
    {"id" : "23-sc-4114","name": "Jasmin Rose Villanueva", "age": 22}
]

with open("student.json", "w", newline="" , encoding="utf-8") as file:
    field_names = ["id","name","age"]
    writer = json.dump(students,file,indent=1) 

with open("student.json", "r", newline="" , encoding="utf-8") as file:
    reader = json.loads(file)


for student in reader:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("-" * 20)
