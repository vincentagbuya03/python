import json
import crudfunction as crudfunction



def menu():
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        login()
    elif choice == 2:
        register()
    elif  choice == 3:
        print("Thankyou for using this system")
        break
    else:
        print("Incorrect input pls try again")
        menu()


def login():
    return

def register():
    username = input("Enter your username : ")
    password = input("Enter your password : ")