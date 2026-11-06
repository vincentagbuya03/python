# ==========================================
# 1. PRINT & OUTPUT EXAMPLES
# ==========================================
print("Hello, World!")

# Using f-strings to insert variables into text
name = "Vincent"
age = 20
print(f"My name is {name} and I am {age} years old.")


# ==========================================
# 2. INPUT EXAMPLES
# ==========================================
# Getting text (string)
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")

# Getting a whole number (integer)
num = int(input("Enter a whole number: "))
print(f"Double your number is: {num * 2}")

# Getting a decimal number (float)
temp = float(input("Enter temperature in Fahrenheit: "))
celsius = (temp - 32) * 5 / 9
print(f"Temperature in Celsius: {celsius:.2f}")


# ==========================================
# 3. IF - ELIF - ELSE (CONDITIONS)
# ==========================================
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: Failed")


# ==========================================
# 4. ARRAYS / LISTS (STORING MULTIPLE ITEMS)
# ==========================================
# In Python, arrays are called "Lists"
names = ["Alice", "Bob", "Charlie"]

# 1. Access items by index (starts at 0)
print(f"First item: {names[0]}")
print(f"Last item: {names[-1]}")

# 2. Add new items
names.append("David")          # Adds to the end
names.insert(1, "Vincent")     # Adds at index 1

# 3. Remove items
names.remove("Bob")            # Removes "Bob"
removed_person = names.pop()   # Removes and returns the last item

# 4. Check length (how many items)
print(f"Total names: {len(names)}")

# 5. Check if an item exists
if "Vincent" in names:
    print("Vincent is in the list!")


# ==========================================
# 5. FOR LOOPS (REPEATING CODE)
# ==========================================
# Count numbers 1 to 5
print("\nCounting 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

# Loop through our array / list
print("\nNames in my list:")
for person in names:
    print(f"- {person}")


# ==========================================
# 6. WHILE LOOP (SIMPLE MENU SYSTEM)
# ==========================================
# A list to store items added by the user
todo_list = ["Learn Python", "Practice Code"]

while True:
    print("\n--- SIMPLE MENU ---")
    print("1. View To-Do List")
    print("2. Add Item to To-Do List")
    print("3. Kilometers to Miles Converter")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"  {idx}. {task}")

    elif choice == "2":
        new_task = input("Enter a new task: ")
        todo_list.append(new_task)
        print(f"Added: '{new_task}'")

    elif choice == "3":
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print(f"{km} km = {miles:.2f} miles")

    elif choice == "4":
        print("Goodbye!")
        break  # Stops the while loop

    else:
        print("Invalid choice, please enter 1, 2, 3, or 4.")
