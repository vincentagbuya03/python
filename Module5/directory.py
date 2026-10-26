# from pathlib import Path

# file_path = Path("data") / "student.txt"

# print(file_path)


# with open("student.txt", "r" , encoding="utf-8") as file:
#     print(file.readline(), end="")
name = []
change = ""
found = False


count = int(input("Enter the number of student: "))



for i in range(count):
    name.append(input("Enter name of student: "))

    
with open("student.txt" , "w" , encoding="utf-8") as file :
    for i in name:
        file.write(f"{i}\n")
find = input("Enter the name you want to find : ")

with open("student.txt" , "r" , encoding="utf-8") as file :
    for i in file:
        if i.strip() == find.strip():
            print("Exist")
            found = True
            break
    if not found:
        print("Not Found")