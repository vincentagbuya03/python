nvda_name = input("Enter your name: ")
nvda_age = int(input("Enter your age: "))
nvda_midterm = float(input("Enter your Mid Grade : "))
nvda_finalgrade = float(input("Enter your Final Grade : "))

nvda_average = (nvda_midterm + nvda_finalgrade) / 2

line = "="
print(line*20)
print("Student Evaluation")
print(line*20)
print(f"Average:{nvda_average}")
print(f"Passing : {nvda_average>=75 and nvda_average <=100}")
print(f"At least 18 years old: {nvda_age>=18}")
print(f"Qualified : {nvda_average>=75 and nvda_age>=18}")
print(line*20)
