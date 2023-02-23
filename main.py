

def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return "Can not divide on zero"
    else:
        return first_number / second_number


print("Welcome to calculator!")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second second: ")) # Переменые можно было сделать покороче
operation = input("Enter the operation (+, -, *, /)")


if operation == '+':
    result = add(first_number, second_number)
elif operation == '-':
    result = subtract(first_number, second_number)
elif operation == '*':
    result = multiply(first_number, second_number)
elif operation == '/':
    result = divide(first_number,second_number)
else:
    print("Invalid operation")


print(f"result': {result}")
