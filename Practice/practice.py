# Practice 1: Student Information & Grades
import functools

studentID = input("Student ID : ")
name = input("Student Name : ")
age = int(input("Age :"))
course = input("Course : ")
yearlevel = int(input("Year Level : "))
prelimGrade = float(input("Prelim : "))
midGrade = float(input("Midterm : "))
final = float(input("Final : "))
average = (prelimGrade + midGrade + final) / 3
passing = (average >= 75)
qualified = (age >= 18 and average >= 75)
print("==============================")
print("     Student Information      ")
print("==============================")
print(f"Student ID : {studentID}")
print(f"Student Name : {name}")
print(f"Age : {age}")
print(f"Course : {course}")
print(f"Year Level : {yearlevel}")

print()
print("Grades")
print("-------------------------")
print(f"Prelim : {prelimGrade:.2f}")
print(f"Midterm : {midGrade:.2f}")
print(f"Final : {final:.2f}")
print(f"Average : {average:.2f}")
print("==========================")

if qualified:
    print("Congratulations! You are qualified.")
else:
    print("Sorry! You are not qualified.")

# ==========================================
# Practice 2: List and Dictionary Operations
# ==========================================
# students = [
#     {"name": "Vincent Agbuya", "age": 21, "is_student": True},
#     {"name": "Glend Allyzza Loresco", "age": 22, "is_student": True},
#     {"name": "Jasmin Rose Villanueva", "age": 22, "is_student": True},
#     {"name": "Sir Napoleon Hermoso", "age": 32, "is_student": False},
#     ]

# for i in range(len(students)):
#     if(students[i]["age"] <= 21):
#         print(students[i]["name"])

# for i in range(len(students)):
#     print(students[i])

# numbers = [10 , 20 , 30 , 40]
# add = int(input("Enter how many index : "))
# for i in range(add):
#     numbers.extend([int(input("Enter value : "))])

# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
