# def multiply_func(a, b):
#     result = a * b
#     return int(result)
#
#
# def divide_func(a, b):
#     result = a / b
#     return int(result)
#
#
# def add_func(a, b):
#     result = a + b
#     return int(result)
#
#
# def subtract_func(a, b):
#     result = a - b
#     return int(result)
#
#
# operation = input()
# a = int(input())
# b = int(input())
#
# if operation == "multiply":
#     print(multiply_func(a, b))
# elif operation == "divide":
#     print(divide_func(a, b))
# elif operation == "add":
#     print(add_func(a, b))
# elif operation == "subtract":
#     print(subtract_func(a, b))

def score(a, b , operation):
    if operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = a / b
    elif operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    return int(result)


type_of_operation = input()
num_a = int(input())
num_b = int(input())
print(score(num_a, num_b, type_of_operation))