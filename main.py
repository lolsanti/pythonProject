def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


def divide(num_1, num_2):
    if num_2 == 0:
        return "Can't divide by zero"
    else:
        return num_1 / num_2


print("Welcome to Calculator!")
while True:
    try:
        num1 = float(input("Enter the first number: "))
    except:
        num1 = float(input("It's should be a number: "))

    try:
        num2 = float(input("Enter the second number: "))
    except:
        num2 = float(input("It's should be a number: "))

    operation = input("Enter an operation (+, -, *, /): ")

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Incorrect operation!")
        continue

    print(f"result: {result}")

    again = input("Do you want to continue? (yes/no): ")
    if again.lower() != "yes":
        break

print("Thank you for using the calculator!")
