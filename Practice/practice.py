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
qualified = (age >= 18  and average >= 75)
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



# print(f"Average : {average}")
# print(f"Passing : {passing}")
# print(f"At least 18 years old : {age >= 18}" )
# print(f"Qualified : {qualified}")
if qualified:
    print("Congratulations! You are qualified.")
else:
    print("Sorry! You are not qualified.")