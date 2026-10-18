# Store accounts in lists (plural names so they don't get overwritten)
usernames = ["nick", "vincent", "agbuya"]
passwords = ["12345", "67890", "12345"]

while True:
    print("\n--- LOGIN MENU ---")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        user_input = input("Enter your username: ")
        pass_input = input("Enter your password: ")


        if user_input in usernames:
            user_index = usernames.index(user_input)  # Find position of username
            if passwords[user_index] == pass_input:   # Check password at same position
                print(f"Login successful! Welcome, {user_input}.")
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")

    elif choice == "2":
        new_user = input("Enter a new username: ")
        new_pass = input("Enter a new password: ")

        # Prevent duplicate usernames
        if new_user in usernames:
            print("That username is already taken! Try another one.")
        else:
            usernames.append(new_user)
            passwords.append(new_pass)
            print("Registration successful!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please enter 1, 2, or 3.")