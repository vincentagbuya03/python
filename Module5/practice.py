def add(num1 , num2):
    return print(num1 + num2)
def subtract(num1 , num2):
    return print(num1 + num2)
def multiply(num1 , num2):
    return print(num1 + num2)
def divide(num1 , num2):
    return print(num1 + num2)

def operation(choice):
    if(choice == "+"):
        add(num1,num2)
    elif(choice == "-"):
        subtract(num1,num2)
    elif(choice == "*"):
        multiply(num1,num2)
    elif(choice == "/"):
        divide(num1,num2)
    else:
        print("Try Again : ")    

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

choice = input("Enter Operation + - * / : ")

operation(choice)


