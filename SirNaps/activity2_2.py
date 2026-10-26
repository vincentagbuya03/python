nvda_firstname = input("Enter First Name : ")
nvda_lastname = input("Enter Last Name : ")
nvda_course = input("Enter Course : ")
nvda_fullname = nvda_firstname +" "+ nvda_lastname
line = "="
print(line*20)
print("String Information")
print(line*20)

print("Full Name : " + nvda_firstname.capitalize() +" " +  nvda_lastname.capitalize())
print("Upper Case : " + nvda_firstname.upper() + " " +  nvda_lastname.upper())
print("Lower Case : " + nvda_firstname.lower() + " " +  nvda_lastname.lower())
print("Title Case : " + nvda_firstname.title() + " " + nvda_lastname.title())
print(f"Number of Character {len(nvda_fullname)}" )
print("First Character : " + nvda_firstname[0].upper())
print("Last Character : " + nvda_lastname[-1])
print("Course : " + nvda_course.title())
print(line*20)
