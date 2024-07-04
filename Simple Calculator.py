#Simple Calculator
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        return "Error: Division by Zero!"
    else:
        return a / b

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter Your Choice(1/2/3/4): ")

    num1 = float(input("Enter Your First Number: "))
    num2 = float(input("Enter Your Second Number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")
        

calculator()

