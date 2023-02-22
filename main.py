

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
second_number = float(input("Enter the second second: "))
operation = input("Enter the operation (+, -, *, /)")
# Переменые можно было сделать покороче

print(add(first_number, second_number))
print(subtract(first_number, second_number))
print(multiply(first_number, second_number))
print(divide(first_number, second_number))


