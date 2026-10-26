# # students = [
# #     {"name": "Vincent Agbuya", "age": 21, "is_student": True},
# #     {"name": "Glend Allyzza Loresco", "age": 22, "is_student": True},
# #     {"name": "Jasmin Rose Villanueva", "age": 22, "is_student": True},
# #     {"name": "Sir Napoleon Hermoso", "age": 32, "is_student": False},
# # ]

# line = "-"
# students = {
#     "student_011":{"name": "Vincent Agbuya", "age": 21, "is_student": True},
#     "student_002": {"name": "Glend Allyzza Loresco", "age": 22, "is_student": True},
#     "student_003": {"name": "Sir Napoleon Hermoso", "age": 32, "is_student": False},
#     "student_004": {"name": "Jasmin Rose Villanueva", "age": 22, "is_student": True}
#     }

# def addStudent():

#     print((line * 5) ,"Add Student" , (line * 5) )
#     student_id = input("Enter Student ID : ")
#     name = input("Enter student name : ")
#     age = int(input("Enter student age : "))
#     is_student = input("Is it student?  True/False  : ").lower() == "true"
#     students[student_id] = {"name" : name , "age": age , "is_student" : is_student}
#     print("Student Added")


# def viewStudents():
#     print((line * 5) ,"All Student List" , (line * 5) )
#     for student_id , student_info in students.items():
#         print(f"ID: {student_id}, Name: {student_info['name']}, Age: {student_info['age']}, Is Student: {student_info['is_student']}")
#     print("")

# def deleteStudent():
#     print((line * 5) ,"Delete Student" , (line * 5) )
#     student_id = input("Enter student ID : ")
#     if student_id in students:
#         del students[student_id]
#         print("Student Deleted")
#     else:
#         print("Student not found")

# def searchStudent():
#     print((line * 5) ,"Search Student" , (line * 5) )
#     student_id = input("Enter student ID : ")
#     if student_id in students:
#         print("\033[H\033[J")
#         print(f"{student_id}, {students[student_id]['name']}")
#     else:
#         print("\033[H\033[J")
#         print("Student not found")   

# while(True):
#     print("")
#     print("1.) Add Student")
#     print("2.) View Students")              
#     print("3.) Delete Student")
#     print("4.) Search Student")
#     print("5.) Exit")
#     choice = int(input("Enter a choice : "))
    
#     if choice == 1: 
#         print("\033[H\033[J")
#         addStudent()
#     elif choice == 2:
#         print("\033[H\033[J")
#         viewStudents()
#     elif choice == 3: 
#         print("\033[H\033[J")
#         deleteStudent()
#     elif choice == 4:
#         print("\033[H\033[J")
#         searchStudent()
#     elif choice == 5:
#         print("\033[H\033[J")
#         print("Exiting program...")
#         break
#     else:
#         print("")
#         print("\033[H\033[J")
#         print("Invalid input, Please try again...")


class Student:
    def __init__(self, name):
        self.name = name
        print(f"Student {self.name} has been created.")

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    def set_age(self, age):
        self.age = age
        print(f"Student {self.name} is {age} years old.")

    def get_age(self):
        if hasattr(self, 'age'):
            return self.age
        else:
            print(f"Age not set for student {self.name}.")
            return None


student_name = input("Enter student's name: ")
student_age = int(input("Enter your age: "))
student = Student(student_name)
student.greet()
age = student.get_age()
if age is not None:
    print(f"The student's age is {age}.")
    