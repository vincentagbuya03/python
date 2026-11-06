nvda_name = input("Enter your name: ")
nvda_grade = int(input("Enter your average: "))
nvda_attendance_percentage = int(input("Enter your attendance percentage: "))
nvda_disciplinary_action = int(input("Number of disciplinary actions : "))

line = "="
if nvda_grade >= 75 and nvda_attendance_percentage >= 75 and nvda_disciplinary_action == 0:
    print(line * 50)
    print("Results of screening for scholarship eligibility")
    print(line * 50)
    print(f"{nvda_name}, you are eligible for the scholarship.")
else:
    print(line * 50)
    print("Results of screening for scholarship eligibility")
    print(line * 50)
    print(f"{nvda_name}, you are not eligible for the scholarship.")