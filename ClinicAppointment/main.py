
import file_operations
import csv

def register_account():
    username = input("Enter username : ")
    password = input("Enter password : ")


    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(", ")
                if parts and parts[0].lower() == username.lower():
                    print("Username already exists!")
                    return
    except FileNotFoundError:
        pass

    with open("users.txt", "a", encoding="utf-8") as file:
        file.write(f"{username}, {password}\n")
    print("Account registered successfully")


def login():
    username = input("Enter username : ")
    password = input("Enter password : ")

    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == f"{username}, {password}":
                    print("Login Successful")
                    loggedin()
                    return
        print("Invalid username or password")
    except FileNotFoundError:
        print("No accounts found. Please register an account first.")


def display_appointment():
    file_operations.view_appointment()


def search_appointment():
    file_operations.search_appointment()


def count_appointment_by_date():
    file_operations.count_appointment_by_date()


def loggedin():
    while True:
        print("\n1. Register Patient Appointment")
        print("2. View Patient Appointment")
        print("3. Search Patient Appointment")
        print("4. Count Appointments by Date")
        print("5. Logout")
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            file_operations.register_appointment()
        elif choice == 2:
            display_appointment()
        elif choice == 3:
            search_appointment()
        elif choice == 4:
            count_appointment_by_date()
        elif choice == 5:
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")


def menu():
    while True:
        print("\n1. Register Account")
        print("2. Login")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 3.")
            continue

        if choice == 1:
            register_account()
        elif choice == 2:
            login()
        elif choice == 3:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


menu()



