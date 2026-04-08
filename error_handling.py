# Debugging Techniques

# print("Hello, world!" # SyntaxError: unexpected EOF while parsing
# print(name) # NameError: name 'name' is not defined
# 5 + "5" # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# my_list = [1, 2, 3]
# print(my_list[5]) # IndexError: list index out of range
# num = 42
# num.append(5) # AttributeError: 'int' object has no attribute 'append'

# Common Debugging techniques
# Using the print function and f-strings
# def add(a, b):
#     result = a + b
#     print(f'Adding {a} and {b} gives {result}')
#     return result

# add(2,5)


# Interactive Debugging with the pdb Module
# import pdb

# def divide(a, b):
#     pdb.set_trace() # you can step through the code, inspect variables, and understand the program's behavior
#     return a / b

# print(divide(10, 2))

# IDE Debugging Tools - VS Code Debugger
# def divide(a, b):
#     result = a / b
#     return result

# print(divide(10, 2))
# print(divide(15, 3))

# Exception Handling
# Example 1
# try: # anticipate an error might occur
#     x = 10 / 0
# except ZeroDivisionError:  # runs if an error of the specified type is raised inside the try
#     print("You can't divide by zero!")

# Example 2
# try:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# else: # Runs if no exception is raised in the try block
#     print('Division successful:', x)
# finally: # Runs no matter what—whether or not an exception occurred. Useful for clean-up tasks like closing files or releasing resources.
#     print('This block always runs.')

# Example 3
# try:
#     number = int('abc')
#     result = 10 / number
# except ValueError: # multiple exceptions with separate except blocks
#     print('That was not a valid number.')
# except ZeroDivisionError:
#     print("Can't divide by zero.")

# try:
#     x = 1 / 0
# except ZeroDivisionError as e: # e lets you access the actual error message or object for logging or debugging
#     print(f'Error occurred: {e}')

# try:
#     number = int(input('Enter a number: '))
#     result = 10 / number
# except (ValueError, ZeroDivisionError) as e: # multiple exceptions in a single except clause by specifying the exceptions as a tuple
#     print(f'Error occurred: {e}') 


# Raise Statement
# Is used to explicitly throw an exception at any point in your program, allowing you to signal that an error condition has occurred or that certain requirements haven't been met

# def check_age(age):
#     if age < 0:
#         raise ValueError('Age cannot be negative')
#     return age

# try:
#     check_age(-5)
# except ValueError as e:
#     print(f'Error: {e}') # Error: Age cannot be negative


# def process_data(data):
#     try:
#         result = int(data)
#         return result * 2
#     except ValueError:
#         print('Logging: Invalid data received')
#         raise  # Re-raises the same ValueError

# try:
#     process_data('abc')
# except ValueError:
#     print('Handled at higher level')


# def calculate_square_root(number):
#     assert number >= 0, 'Cannot calculate square root of negative number' # shorthand for raise with AssertionError
#     return number ** 0.5

# try:
#     result = calculate_square_root(-4)
# except AssertionError as e:
#     print(f'Assertion failed: {e}')