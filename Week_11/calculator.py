#basic calculator
import sys

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("welcome, input the operation you want to perform")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True:
    choice = input("Enter operation by number (1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4'):
        num1 = int(input("enter your first number: "))
        num2 = int(input("enter your second number: "))
        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "3":
            print(num1, "x", num2, "=", multiply(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == "5":
            sys.exit()
    else:
        print("invalid input")