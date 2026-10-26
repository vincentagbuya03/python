# grades = [80, 90, 100]
# change = 0

# # Write grades to file
# with open("student.txt", "w", encoding="utf-8") as file:
#     for grade in grades:
#         file.write(f"{grade}\n")

# # Read grades from file
# with open("student.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     change = lines[1].strip()  # Remove newline character

# print(change)
# change = "10"  # Correctly assign a string
# print(change)

# # Write the new grade back to the file
# with open("student.txt", "w", encoding="utf-8") as file:
#     for i, line in enumerate(lines):
#         if i == 1:
#             file.write(change + "\n")
#         else:
#             file.write(line)

# students = {
#     "student_011": {"name": "Vincent Agbuya", "age": 21, "is_student": True},
#     "student_002": {"name": "Glend Allyzza Loresco", "age": 22, "is_student": True},
#     "student_003": {"name": "Sir Napoleon Hermoso", "age": 32, "is_student": False},
#     "student_004": {"name": "Jasmin Rose Villanueva", "age": 22, "is_student": True}
# }


# with open("student.txt", "w", encoding="utf-8") as file:
#     for student_id, details in students.items():
#         file.write(f"{student_id}: {details}\n")

# find = input("Enter Student ID : ")


with open("student.txt", "r", encoding="utf-8") as file:
    found = False
    for line in file:
        if line.startswith(find):
            print("Exist:", line.strip())
            found = True
            break
    if not found:
        print("Not Found")