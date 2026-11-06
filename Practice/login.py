username = ["vincent" , "nick"]
password = ["1234" , "5678"]

user = input("Enter your username : ")
passw = input("Enter your password :")

if user in username:
    index = username.index(user)
    if password[index] == passw:
        print(f"Login successful! Welcome, {user}.")
    else:
        print("Incorrect Password.")
else:
    print("Username not found.")

