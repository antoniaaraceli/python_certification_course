# This notes are taken by me for the Python Certification Course by FreeCodeCamp.

#### Python Basics
### What is Python?
""" 
Introduction: Python is a general-purpose programming language known for its simplicity and ease of use. Python is used in many fields like data science and machine learning, web development, scripting and automation, embedded systems and IoT, and much more.
Common Use Cases: Python is used in data science, machine learning, web development, cybersecurity, automation and microcomputers like the Raspberry Pi and MicroPython-compatible boards. 
"""

#### VARIABLES & DATA TYPES

#### STRINGS
## Characters surrounded by single quotes are treated equally than characters surrounded by double quotes
# str1 = 'Hola'
# str2 = "Hola" 
## Multi-line string
# str3 = ''' Hola
# Mundo'''
# str4 = """Hola
# Mundo"""
## If your string contains either single or double quotation marks
# msg = "It's a sunny day!"
# quote = 'She said, "Hello!"'
## or
# msg2 = 'It\'s a sunny day!'
# quote2 = "She said, \"Hello!\""
## Check if a string contains one or more characters
#check_str = 'Hola Mundo'
# print('Hola' in check_str) # true
# print('U' in check_str) # false, case-insensitive
## Length and indexing
#len_str = 'Hola mundo'
# print(len(len_str))
# print(len_str[0]) # H
# print(len_str[-1]) # o

## NOTE: all data gets treated as objects, and some objects are immutable while others are mutable. Strings are immutable data types in Python. 
## You can reassign but you can't change the original object itself
# greeting = 'hi'
# greeting = 'hello'
# print(greeting) # hello
# greeting[0] = 'H' # TypeError: 'str' object does not support item assignment

## NOTE: Other immutable data types in Python are integer, float, boolean, tuple, and range.

### Concatenation and Interpolation
## You can convert a number into a string with the built-in str() function
# name = 'Joe Doe'
# age = 23
# name_and_age = name + str(age)
# print(name_and_age)

## F-strings: allow you to embed variables or expressions inside replacement fields indicated by curly braces ({})
#name_and_age2 = f'Hi, my name is {name} and I\'m {age} years old.'
# print(name_and_age2)


### Slicing
## String slicing lets you extract a portion of a string or work with only a specific part of it. Here's the basic syntax: string[start:stop]. The stop index is non-inclusive.
#sli_str = 'Hola Mundo!'
# print(sli_str[0:3]) # Hol
# print(sli_str[:4]) # Hola
# print(sli_str[3:]) # a Mundo
## there's also an optional step parameter, which is used to specify the increment between each index in the slice. string[start:stop:step]
# print(sli_str[0:10:3]) # Hauo
## There's a helpful trick to reverse a string by setting step to -1, and leaving start and stop blank:
#print(sli_str[::-1]) # !odnuM aloH

### String Methods
#str = 'Hola Mundo'
# print(str1.upper()) # HOLA MUNDO
# print(str.lower()) # hola mundo
#str2 = ' Hola Mundo '
# print(str2.strip()) # Hola Mundo, without spaces
# print(str.replace('Hola', 'Adiós')) # Adiós mundo
# print(str.split()) # ['Hola', 'Mundo'] -> If no separator is specified, it splits on whitespace.

# my_gretting = ['Hola', 'Mundo']
# joined_str = ' '.join(my_gretting)
#print(joined_str) # Hola Mundo
#print(str.startswith('H')) # True
#print(str.endswith('x')) # False
#print(str.find('Mundo')) # 5 -> Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
#print(str.count('o')) # 2 -> Returns the number of times a substring appears in a string.
#print(str.lower().capitalize()) # Hola mundo
#print(str.lower().title()) # Hola Mundo


### Conditional Statements and Logical Operators 
## if statement
#age = 12
#if age >= 18:
#    print('Enjoy your drinks!')
#elif age >= 12:
#    print('Soda for you!')
#else:
#    print('There is some juice for you')


### FUNCTIONS
## input()
#name = input('¿Cómo te llamas? ')
#def saludo():
#    print('Hola', name)

#saludo()

#def calculo_imc(peso, altura):
#    return peso / (altura ** 2)

#print(calculo_imc(84, 1.72))

### Scope
# Python follows the LEGB rule, which stands for the following:
## Local scope (L): Variables defined in functions or classes.
#def my_func():
#    my_var = 10
#    print(my_var)
#my_func() # 10
#print(my_var) # NameError: name 'my_var' is not defined

## Enclosing scope (E): Variables defined in enclosing or nested functions.
#def outer_func():
#    msg = 'Hello there!'
#    print(res)

#    def inner_func():
#       res = 'How are you?'
#        print(msg)

#    inner_func()

#outer_func() # Hello there!
#outer_func() # NameError: name 'res' is not defined

## Global scope (G): Variables defined at the top level of the module or file.
# my_var = 100
# my_var_1 = 7

# def show_var():
#     print(my_var)

# show_var() # 100
# print(my_var) # 100

# def show_var1():
#     global my_var_2
#     my_var_2 = 10
#     print(my_var_1)
#     print(my_var_2)

# show_var1() # 7 10
# # my_var_2 is now a global variable and can be accessed anywhere in the program
# print(my_var_2) # 10

# Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
