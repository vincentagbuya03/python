
import os
import sys
import file_operations
import csv
import getpass
import hashlib

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_masked_input(prompt="Enter password : ", mask="*"):
    """Prompt for a password while displaying masked characters (e.g. ***)."""
    if not sys.stdin.isatty():
        try:
            return getpass.getpass(prompt)
        except Exception:
            return input(prompt)

    sys.stdout.write(prompt)
    sys.stdout.flush()
    password = []

    if os.name == 'nt':
        import msvcrt
        while True:
            ch = msvcrt.getwch()
            if ch in ('\r', '\n'):
                sys.stdout.write('\n')
                sys.stdout.flush()
                break
            elif ch == '\x08':  # Backspace
                if password:
                    password.pop()
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            elif ch == '\x03':  # Ctrl+C
                raise KeyboardInterrupt
            elif ch in ('\x00', '\xe0'):  # Arrow keys / special characters
                msvcrt.getwch()
            else:
                password.append(ch)
                sys.stdout.write(mask)
                sys.stdout.flush()
    else:
        import tty
        import termios
        import select
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch in ('\r', '\n'):
                    sys.stdout.write('\r\n')
                    sys.stdout.flush()
                    break
                elif ch in ('\x7f', '\x08'):  # Backspace or DEL
                    if password:
                        password.pop()
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                elif ch == '\x03':  # Ctrl+C
                    raise KeyboardInterrupt
                elif ch == '\x04':  # Ctrl+D
                    break
                elif ch == '\x1b':  # Arrow keys / escape sequence
                    if select.select([sys.stdin], [], [], 0.05)[0]:
                        sys.stdin.read(2)
                else:
                    password.append(ch)
                    sys.stdout.write(mask)
                    sys.stdout.flush()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ''.join(password)

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_account():
    clear_console()
    username = input("Enter username : ")
    password = get_masked_input("Enter password : ", mask="*")


    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(", ")
                if parts and parts[0].lower() == username.lower():
                    print("Username already exists!")
                    return
    except FileNotFoundError:
        pass

    hashed_password = hash_password(password)
    with open("users.txt", "a", encoding="utf-8") as file:
        file.write(f"{username}, {hashed_password}\n")
    print("Account registered successfully")


def login():
    clear_console()
    username = input("Enter username : ")
    password = get_masked_input("Enter password : ", mask="*")

    hashed_password = hash_password(password)

    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) >= 2:
                    stored_username = parts[0]
                    stored_password = parts[1]
                    if stored_username == username and (stored_password == hashed_password or stored_password == password):
                        clear_console()
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
        print("2. Display All Appointment")
        print("3. Search Appointment")
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
            clear_console()
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")


def menu():
    clear_console()
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
            clear_console()
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


menu()



