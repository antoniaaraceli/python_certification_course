# Dictionaries are built-in data structures that store collections of key-value pairs
# pizza = {
#     'name': 'Margherita Pizza',
#     'price': 8.9,
#     'calories_per_slice': 250,
#     'toppings': ['mozzarella', 'basil']
# }

# # using the dict() constructor
# pizza_const = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

# print(pizza['name'])

# pizza['name'] = 'Margherita'
# print(pizza['name'])

# # .get() method retrieves the value associated with a key
# print(pizza.get('toppings', []))

# # The .keys() and .values() methods return a view object with all the keys and values in the dictionary
# pizza.keys() # dict_keys(['name', 'price', 'calories_per_slice'])
# pizza.values() # dict_values(['Margherita Pizza', 8.9, 250])

# pizza.items() # returns a view object with all the key-value pairs in the dictionary
# pizza.clear() # removes all the key-value pairs from the dictionary
# print(pizza.pop('price', 10)) # removes the key-value pair with the key that you specify as the first argument and returns its value
# # pizza.pop('total_price') # KeyError
# pizza.popitem() # removes the last inserted item
# pizza.update({ 'price': 15, 'total_time': 25 })

# Techniques to Loop Over a Dictionary
# products = {
#     'Laptop': 990,
#     'Smartphone': 600,
#     'Tablet': 250,
#     'Headphones': 70,
# }

# for product, price in products.items():
#     products[product] = round(price * 0.8)
    
# print(products)

# for product in enumerate(products):
#     print(product) # iterate over the key-value pairs while keeping track of a counter

# SETS -> they don't store duplicate values, are mutable and unordered.
# To define a set, you just need to write its elements within curly braces and separate them with commas.
# set() # Set
# {}    # Dictionary
# my_set = {1, 2, 3, 4, 5} 
# my_set.add(6)
# print(my_set) # {1, 2, 3, 4, 5, 6}
# my_set.add(5)
# print(my_set) # {1, 2, 3, 4, 5, 6}, If you try to add an element that is already in the set, only one will be kept.
# my_set.remove(4) # will raise a KeyError if the element is not found
# my_set.discard(4)
# my_set.clear() # removes all the elements from the set

# my_set = {1, 2, 3, 4, 5}
# your_set = {2, 3, 4, 6}

# print(your_set.issubset(my_set)) # False
# print(my_set.issuperset(your_set)) # False
# print(my_set.isdisjoint(your_set)) # False -> they don't have any elements in common.
# my_set | your_set # {1, 2, 3, 4, 5, 6} -> returns a new set with all the elements from both sets
# my_set & your_set # {2, 3, 4} -> returns a new set with only the elements that the sets have in common
# my_set - your_set # {1, 5} -> returns a new set with the elements of the first set that are not in the other sets
# my_set ^ your_set # {1, 5, 6} -> returns a new set with the elements that are either in the first or the second set
# my_set -= your_set # {1, 5} -> finds the difference between the sets and updates the first set with that result
# # Also aplies for |= &= -= ^=
# print(5 in my_set) # check if an element is in a set or not 

# A regular expression, or regex, is a pattern used to match a sequence of characters in text. The search function from the re module takes a regex pattern and a string as its arguments.

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product in products.items():
    print(product)