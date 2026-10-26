nvda_id = input("Enter your ID: ")
nvda_name = input("Enter your name: ")
nvda_age = int(input("Enter your age: "))
nvda_course = input("Enter Course : ")
nvda_yearlevel = int(input("Enter your year level: "))

nvda_midterm = float(input("Midterm: "))
nvda_final = float(input("Final: "))
nvda_average = (nvda_midterm + nvda_final) / 2


nvda_campus = "San Carlos"
nvda_yearnow = 2026
lineone = "-"
line = "="
print(line*20)
print("STUDENT GRADE REPORT")
print(line*20)


print(f"Student ID: {nvda_yearnow}-{nvda_campus[0:6:4]}-{nvda_id}")
print(f"Student Name {nvda_name.title()}")
print(f"Age: {nvda_age}")
print(f"Course {nvda_course.title()}")
print(f"Year Level {nvda_yearlevel}")

print(lineone*20)
print("GRADES")
print(lineone*20)

print(f"Midterm: {nvda_midterm}")
print(f"Final: {nvda_final}")
print(f"Average: {(nvda_midterm + nvda_final) / 2}")


print(lineone*20)
print("EVALUATION")
print(lineone*20)
print(f"PASSING: {nvda_average>=75}" )
print(f"ADULT: {nvda_age>=18}" )
print(f"QUALIFIED: {nvda_average>=75 and nvda_age>=18}" )