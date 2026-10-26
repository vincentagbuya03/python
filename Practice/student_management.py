students = {
    "student_011": {"name": "Vincent Agbuya", "age": 21, "is_student": True},
    "student_002": {"name": "Glend Allyzza Loresco", "age": 22, "is_student": True},
    "student_003": {"name": "Sir Napoleon Hermoso", "age": 32, "is_student": False},
    "student_004": {"name": "Jasmin Rose Villanueva", "age": 22, "is_student": True}
}

def addStudent():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    is_student = input("Is the student a student? (True/False): ").lower() == "true"
    students[student_id] = {"name": name, "age": age, "is_student": is_student}
    print("Student added successfully!")

def viewStudents():
    for student_id, student_info in students.items():
        print(f"ID: {student_id}, Name: {student_info['name']}, Age: {student_info['age']}, Is Student: {student_info['is_student']}")

def deleteStudent():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def searchStudent():
    student_id = input("Enter student ID to search: ")
    if student_id in students:
        student_info = students[student_id]
        print(f"ID: {student_id}, Name: {student_info['name']}, Age: {student_info['age']}, Is Student: {student_info['is_student']}")
    else:
        print("Student not found!")

while True:
    print("\n1.) Add Student")
    print("2.) View Students")
    print("3.) Delete Student")
    print("4.) Search Student")
    print("5.) Exit")
    choice = int(input("Enter a choice : "))

    if choice == 1:
        addStudent()
    elif choice == 2:
        viewStudents()
    elif choice == 3:
        deleteStudent()
    elif choice == 4:
        searchStudent()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")