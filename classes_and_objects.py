# How Do Classes Work and How Do They Differ From Objects?
# A class is like a blueprint or template you use to create objects with.
# Here's the basic syntax of a class:
# class ClassName:
#     def __init__(self, name, age): # is a special method that automatically called when a new object is created. It initializes the attributes of the objects that will be created with the class.
#         # The first parameter of __init__ is always a reference to the specific object being created or used. By convention, this parameter is named self.
#         self.name = name
#         self.age = age

#     def sample_method(self): # is the method each object created can call.     
#         print(self.name.upper())

# # Example
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name.upper()} says woof woof!")

# # With this Dog class, you can create an object.
# dog_1 = Dog("Banana", 2)
# dog_2 = Dog("Lorenza", 7)

# # Call the bark method
# dog_1.bark() # BANANA says woof woof!
# dog_2.bark() # LORENZA says woof woof!



## What Are Methods and Attributes, and How Do They Work?
# Attributes are variables that belong to an object, so they hold data. There are two kinds of attributes: instance attributes and class attributes.
# Instance attributes are unique to each object created from a class, and you usually set them with the __init__ method. 
# Class attributes, on the other hand, belong to the class itself and are shared by all instances of that class.
# To access an attribute, you use dot notation.

# class Dog:
#     species = "French Bulldog" # Class attribute

#     def __init__(self, name):
#         self.name = name # Instance attribute

# print(Dog.species) # French Bulldog

# dog1 = Dog("Jack")
# print(dog1.name)    # Jack
# print(dog1.species) # French Bulldog

# dog2 = Dog("Tom")
# print(dog2.name)    # Tom
# print(dog2.species) # French Bulldog
 


## What Are Special Methods and What Are They Used For?
# Special methods in Python, also known as "magic methods" or "dunder methods", are special Python methods that start and end with double underscores (__).
# class Book():
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
#     def __len__(self):
#         return self.pages
#     def __str__(self):
#         return f"'{self.title}' has '{self.pages}' pages."
#     def __eq__(self, other):
#         return self.pages == other.pages
    
# book1 = Book("La Vegetariana", 220)
# book2 = Book("El Cuento de la Criada", 420)

# print(len(book1)) # 220
# print(len(book2)) # 420
# print(str(book1)) # 'La Vegetariana' has 220 pages
# print(str(book2)) # 'El Cuento de la Criada' has 420 pages
# print(book1 == book2) # False

# Here's an example of a Cart class with these user-defined methods and special methods:
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
       return self.items

    def __len__(self):
       return len(self.items)

    def __getitem__(self, index):
       return self.items[index]

    def __contains__(self, item):
       return item in self.items

    def __iter__(self):
       return iter(self.items)

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
   print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor

print(len(cart)) # 4
print(cart[3]) # Monitor

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove('Ergo keyboard')

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana') # banana is not in cart
