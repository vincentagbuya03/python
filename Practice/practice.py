# students = [
#     {"name": "Vincent Agbuya", "age": 21, "is_student": True},
#     {"name": "Glend Allyzza Loresco", "age": 22, "is_student": True},
#     {"name": "Jasmin Rose Villanueva", "age": 22, "is_student": True},
#     {"name": "Sir Napoleon Hermoso", "age": 32, "is_student": False},
#     ]

# for i in range(len(students)):
#     if(students[i]["age"] <= 21):
#         print(students[i]["name"])

# for i in range(len(students)):
#     print(students[i])

numbers = [10 , 20 , 30 , 40]


# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
    
# print("")
# change = int(input("Enter index that you want to change : "))
# value = int(input("Enter value of an index : "))
# numbers.insert(change, value)

# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
# print("")

add = int(input("Enter how many index : "))
for i in range(add):
    numbers.extend([int(input("Enter value : "))])

    
for i in range(len(numbers)):
    print(numbers[i], end=" ")

# numbers.append([50 , 60 , 70] + [80 , 90])

# print(numbers)