# # Loops and sequences
# List data type is an ordered sequence of elements 
# cities = ['Los Angeles', 'London', 'Tokyo']
# cities[0] # 'Los Angeles' -> Access to an element
# cities[-1] # 'Tokyo'
# developer = 'Antonia'
# print(list(developer)) # ['A', 'n', 't', 'o', 'n', 'i', 'a'] -> list() is used to convert an iterable into a list
# print(len(cities)) # 3 -> get the total number of elements
# # To update a value at a particular index
# cities[1] = 'CDMX'
# print(cities)
# del(cities[0]) # ['CDMX', 'Tokyo'] -> remove an element from a list
# print(cities)
# # Check if an element is inside the list
# print('CDMX' in cities) # True
# # Nested list
# developer_profile = ['Antonia', 27, ['Python', 'JS', 'SQL']]
# print(developer_profile[2][1]) # 'JS'
# Unpacking values
# developer = ['Araceli', 27, 'Python Developer']
# name, age, job = developer
# print(name) # 'Araceli'
# print(age) # 27
# print(job) # 'Python Developer'
# # to collect any remaining elements 
# name, *rest = developer
# print(name) # 'Araceli'
# print(rest) # [27, 'Python Developer']
# Slice operator (:)
# desserts = ['Pastel', 'Galletas', 'Helado', 'Pay', 'Brownies']
# print(desserts[1:4]) # ['Galletas', 'Helado', 'Pay']
# numbers = [1, 2, 3, 4, 5, 6]
# print(numbers[1::2]) # [2, 4, 6] -> to extract a list of just even numbers

# Common methods
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6) 
# print(numbers) # [1, 2, 3, 4, 5, 6]
# even_numbers = [7, 8, 9, 10]
# numbers.append(even_numbers) 
# print(numbers) # [1, 2, 3, 4, 5, 6, [7, 8, 9, 10]]
# numbers.extend(even_numbers) 
# print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> extend() method is similar to the append() method, but with extend() you can add multiple elements from one list to another. 
# To insert an element at a specific index in a list
# numbers = [1, 2, 3, 4, 5]
# numbers.insert(2, 'Hola') # [1, 2, 'Hola', 3, 4, 5]
# print(numbers)
# # If you want to remove an element from a list
# numbers.remove('Hola') # [1, 2, 3, 4, 5] -> It is important to note that this method will only remove the first occurrence of an item.
# print(numbers)
# To remove an element at a specific index in the list
# numbers = [1, 2, 3, 4, 5]
# numbers.pop(1) # The number 2 is returned -> If you don't specify an element for the pop method, then the last element is removed.
# print(numbers) # [1, 3, 4, 5]
# # If you need to empty the list, then you can use the clear() method
# numbers.clear()
# print(numbers) # []
# To sort the elements in place
# numbers = [19, 2, 35, 1, 67, 41]
# numbers.sort()
# print(numbers) # [1, 2, 19, 35, 41, 67]
# # In contrast to the sort() method, there is the sorted() function which works for any iterable and returns a new sorted list instead of modifying the original list.
# numbers.reverse() # [67, 41, 35, 19, 2, 1]
# print(numbers)
# To find the first index where an element can be found in a list. 
# programming_languages = ['JS', 'Java', 'Python', 'C++']
# print(programming_languages.index('Python')) # 2

# Tuples
# Is a data type used to create an ordered sequence of values
# Tuples are similar to lists, but while lists are a mutable data type, tuples are immutable. This means that the elements in a tuple cannot be changed once it's created.
# Tuples -> () ->  If you know that you are working with a fixed and immutable collection of data, then you should use a tuple.
# Listas -> [] -> If you need a dynamic collection of elements where you can add, remove and update elements, then you should use a list. 
# developer = 'Araceli' 
# print(tuple(developer)) # ('A', 'r', 'a', 'c', 'e', 'l', 'i')
# If you need to remove an item from a tuple, that isn't possible because tuples are immutable. 
# Common Methods for Tuples
# count() -> This method is used to determine how many times an item appears in a tuple
# programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
# print(programming_languages.count('Rust')) # 2
# # index() -> this method is used to find the index where a particular item is present in a tuple
# print(programming_languages.index('Java')) # 1
# programming_languages2 = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
# print(programming_languages2.index('Python', 3)) # 5
# sorted() -> will always create a new list of the sorted values
# numbers = (13, 2, 78, 3, 45, 67, 18, 7)
# print(sorted(numbers)) # [2, 3, 7, 13, 18, 45, 67, 78]
# programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
# print(sorted(programming_languages, reverse=True)) # ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']

# LOOPS
# for loop
# programming_languages = ['Rust', 'Java', 'Python', 'C++']
# for language in programming_languages:
#     print(language)

# for char in 'code':
#     print(char)
# Nested for loop
# categories = ['Fruit', 'Vegetable']
# foods = ['Apple', 'Carrot', 'Banana']
# for category in categories:
#     for food in foods:
#         print(category, food)

# while loop
# secret_number = 3
# guess = 0
# while secret_number != guess:
#     guess = int(input('Guess the number between 1-5: '))
#     if secret_number != guess:
#         print('Wrong, try again!')

# print('Are you a hacker?! You win!')

# break statement
# developer_names = ['Jess', 'Naomi', 'Tom']
# for dev in developer_names:
#     if dev == 'Tom':
#         break
#     print(dev)

# continue statement: is used to skip the current iteration of a loop and move onto the next iteration
# developer_names = ['Jess', 'Naomi', 'Tom']

# for developer in developer_names:
#     if developer == 'Naomi':
#         continue
#     print(developer)

# words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

# for word in words:
#     for letter in word:
#         if letter.lower() in 'aeiou':
#             print(f"'{word}' contains the vowel '{letter}'")
#             break
#     else:
#         print(f"'{word}' has no vowels")

# The range() function is used to generate a sequence of integers. -> range(start, stop, step)
# for number in range(3):
#     print(number) # 3 is not included because the stop argument is non-inclusive
# for number in range(1, 5):
#     print(number)
# for number in range(1, 10, 2):
#     print(number)
# for number in range(100, 0, -10):
#    print(number) # generate a sequence of integers in decrementing order
# You can create a list of integers by using it with the list constructor
# numbers = list(range(2, 11, 2))
# print(numbers) # [2, 4, 6, 8, 10]

# The enumerate() function keeps track of the index for an iterable and returns an enumerate object.
# languages = ['Spanish', 'English', 'Russian', 'Chinese']
# # print(list(enumerate(languages))) # [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]
# for index, language in enumerate(languages, 1): # also accepts an optional start argument that specifies the starting value for the count. If this argument is omitted, then the count will begin at 0
#     print(f'Index {index} and language {language}')

# The zip() function combines lists into pairs of elements and returns an iterator of tuples
# developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
# ids = [1, 2, 3, 4]
# print(list(zip(developers, ids))) # [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

# for name, id in zip(developers, ids):
#     print(f'Name: {name}')
#     print(f'ID: {id}')

# List comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets.
# even_numbers = [num for num in range(21) if num % 2 == 0]
# print(even_numbers)

# numbers = [1, 2, 3, 4, 5]
# result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
# print(result)

# # filter() function is used to select elements from an iterable that meet a specific condition
# words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

# def is_long_word(word):
#     return len(word) > 4

# long_words = list(filter(is_long_word, words))
# print(long_words) # ['mountain', 'river', 'cloud']

# # map() function takes an iterable and applies a function to each of its elements
# celsius = [0, 10, 20, 30, 40]

# def to_fahrenheit(temp):
#     return (temp * 9/5) + 32

# fahrenheit = list(map(to_fahrenheit, celsius))
# print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

# # sum() function is used to get the sum from an iterable like a list or tuple
# total = sum(celsius)
# print(total)

# print(sum(celsius, 10)) # positional argument

# Lambda Functions
# square() function looks like --> lambda num: num ** 2

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# best practices
# it is not a good practice to assign a lambda function to a variable