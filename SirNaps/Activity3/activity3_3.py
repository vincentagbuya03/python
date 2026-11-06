

default_password = "1234"
attempts = 3
authenticated = False


while attempts > 0:
    entered_password = input("Enter default password: ")
    if entered_password == default_password:
        print("Initial login successful!\n")
        authenticated = True
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. Attempts remaining: {attempts}")
        else:
            print("Access denied.")

if authenticated:
    new_password = input("Change your password (Enter new password): ")
    print("Password changed successfully!\n")

    new_attempts = 3
    access_granted = False



        

    while new_attempts > 0:
        entered_new = input("Enter your new password to login: ")
        if entered_new == new_password:
            print("Login successful! Access granted.\n")
            access_granted = True
            break
        else:
            new_attempts -= 1
            if new_attempts > 0:
                print(f"Incorrect password. Attempts remaining: {new_attempts}")
            else:
                print("Access denied.")


    if access_granted:
        balance = 0.0
        while True:
            print("===== DIGITAL WALLET =====")
            print("1. Check Balance")
            print("2. Add Money")
            print("3. Pay Bill")
            print("4. Transfer Money")
            print("5. Exit")

            choice = input("Enter choice (1-5): ")

            if choice == "1":
                print(f"\nCurrent Balance: {balance:.2f}\n")

            elif choice == "2":
                amount = float(input("\nEnter amount to add: "))
                if amount > 0:
                    balance += amount
                    print(f"Successfully added {amount:.2f}.")
                    print(f"Current Balance: {balance:.2f}\n")
                else:
                    print("Invalid amount. Must be greater than 0.\n")

            elif choice == "3":
                biller = input("\nEnter biller name: ")
                amount = float(input("Enter bill amount: "))
                if amount <= 0:
                    print("Invalid amount. Must be greater than 0.\n")
                elif amount > balance:
                    print("Insufficient balance!\n")
                else:
                    balance -= amount
                    print(f"Successfully paid {amount:.2f} to {biller}.")
                    print(f"Current Balance: {balance:.2f}\n")

            elif choice == "4":
                recipient = input("\nEnter recipient account/number: ")
                amount = float(input("Enter amount to transfer: "))
                if amount <= 0:
                    print("Invalid amount. Must be greater than 0.\n")
                elif amount > balance:
                    print("Insufficient balance!\n")
                else:
                    balance -= amount
                    print(f"Successfully transferred {amount:.2f} to {recipient}.")
                    print(f"Current Balance: {balance:.2f}\n")

            elif choice == "5":
                print("\nThank you for using Digital Wallet. Goodbye!")
                break

            else:
                print("\nInvalid choice! Please select 1 to 5.\n")
