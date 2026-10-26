import csv

students = [
    {"id" : "23-sc-4111","name": "Vincent Agbuya", "age": 21},
    {"id" : "23-sc-4112","name": "Glend Allyzza Loresco", "age": 22},
    {"id" : "23-sc-4113","name": "Sir Napoleon Hermoso", "age": 32},
    {"id" : "23-sc-4114","name": "Jasmin Rose Villanueva", "age": 22}
]

with open("student.csv", "w", newline="" , encoding="utf-8") as file:
    field_names = ["id","name","age"]
    writer = csv.DictWriter(file,fieldnames=field_names)
    writer.writeheader()
    writer.writerows(students)

with open("student.csv", "r", newline="" , encoding="utf-8") as file:
    student = csv.DictReader(file)

    for i in student:
        print(i["id"], i["name"], i["age"])