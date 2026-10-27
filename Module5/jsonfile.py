import json

students = [
    # {"id": "23-sc-4111", "name": "Vincent Agbuya", "age": 21},
    # {"id": "23-sc-4112", "name": "Glend Allyzza Loresco", "age": 22},
    # {"id": "23-sc-4113", "name": "Sir Napoleon Hermoso", "age": 32},
    # {"id": "23-sc-4114", "name": "Jasmin Rose Villanueva", "age": 22}
]
count = int(input("Enter number of student : "))

for i in range(count):
    student_id = input("Enter student id: ")
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    students.append({"student_id" : student_id, "name" : name, "age" : age,})


with open("student.json", "w", newline="", encoding="utf-8") as file:
    json.dump(students, file, indent=1)



with open("student.json", "r", newline="", encoding="utf-8") as file:
    reader = json.load(file)
