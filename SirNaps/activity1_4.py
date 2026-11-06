studentID = input("Student ID : ")
name = input("Student Name : ")
age = int(input("Age :"))
course = input("Course : ")
yearlevel = int(input("Year Level : "))
prelimGrade = float(input("Prelim : "))
midGrade = float(input("Midterm : "))
final = float(input("Final : "))
average = (prelimGrade + midGrade + final) / 3

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
print(f"Prelim : {prelimGrade}")
print(f"Midterm : {midGrade}")
print(f"Final : {final}")
print(f"Average : {average}")
print("==========================")



