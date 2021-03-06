# Python Crash Course
# http://online-courses.club/category/topics/2d-drawing/
"""Hello 
Python 
Lovers!"""


# print(dir())
# print(dir(__builtins__))
# help(locals)


# help('modules') # list of available modules


# Python Errors and Built-in Exceptions
# errors = locals()['__builtins__']
# print(dir(errors))



# Data for practice
# name = 'deva'
# age = 27
# toppings = ['pepper', 'mushroom', 'onions', 'chilli powder']
# hobbies = ('chess', 'drawing', 'story writing')
# numbers = {1, 4, 5, 2, 7, 1, 2, 9, 6, 9, 8, 5}
# person = {
#     'name': 'vasu',
#     'age': 27,
#     'hobbies': ['chess', 'drawing', 'reading'],
#     'address': {
#         'street': 'chocolate factory road',
#         'city': 'bangalore',
#         'state': 'karnataka',
#         'pincode': 530068
#     },
#     'favorite': [{'food': 'dosa'}, 
#     {'cricket': 'sachin','tennis':'roger federer'}]
# }



# dir and help functions
name = 'deva'
age = 27
toppings = ['pepper', 'mushroom', 'onions']
hobbies = ('chess', 'drawing', 'story writing')
numbers = {1, 4, 5, 2, 7, 1, 2, 9, 6, 9, 8, 5}
person = {
    'name': 'vasu',
    'age': 26
}


# print(dir(str))
# print('\n')
# print(dir(int))
# print('\n')
# print(dir(list))
# print("\n")
# print(dir(set))
# print("\n")
# print(dir(tuple))
# print("\n")
# print(dir(dict))
# print("\n")
# print(dir(float))
# print("\n")
# print(dir(complex))
# print("\n")

# print(dir(name))
# print(type(name))
# print(help(name.join))

# print(dir(age))
# print(type(age))
# print(help(age.denominator))

# print(dir(toppings))
# print(type(toppings))
# print(help(toppings.copy))

# print(dir(hobbies))
# print(type(hobbies))
# print(help(hobbies.index))

# print(dir(numbers))
# print(type(numbers))
# print(help(numbers.difference))

# print(dir(person))
# print(type(person))
# print(help(person.fromkeys))
print('\n'*2)


# String

print("Hello Python Lovers!")


name = ' vasudeva tirupathi naidu '
print(name)

print(name.upper())
print(name.capitalize())
print(name.lower())
print(name, len(name), sep='-->')
print(name.rstrip(), len(name.rstrip()), sep='-->')
print(name.lstrip(), len(name.lstrip()), sep='-->')
print(name.strip(), len(name.strip()), sep='-->')
print("\n")

# The order of the characters in the string passed to strip() does not matter
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
print("\n")

email = "tirupathinaidu07@gmail.com"

greet = 'Hello, Deva!'
email = "tirupathinaidu07@gmail.com"

print(greet.upper())
print(greet.lower())
print(greet.isupper())
print(greet.lower().islower())
print(greet.isalpha())
print('abcJHS'.isalpha())
print(email.isalnum())
print('tirupathinaidu 07'.isalnum())
print('tirupathinaidu07'.isalnum())
print('121323412'.isdecimal())
print(' '.isspace())
print('\n'.isspace())
print('\t'.isspace())
print('Vasu Deva'.istitle())

print(email.startswith('t'))
print(email.endswith('.com'))


# Splitting strings with the partition() method
message = 'tirupathinaidu07@gmail.com'.partition('@')
print(message) # tuple of before , seperator(@), after substrings

before, sep, after = 'Hello, world!'.partition(' ')
print(before)
print(after)

message1 = 'hello, world!'.partition('XY')
print(message1)

message2 = 'hello, world!'.partition('o')
print(message2)


# print(dir(email))
# print(help(str))
print(help(str.lower))

print(email)
print(email.upper())
print(email.isupper())
print(email.lower())
print(email.islower())
print(email.title())
print(email.capitalize())
print('@' in email)
print(email[::-1])
print(email[:email.find('0')])
print(email[email.find('@'):])
print(email[email.find('0'):(email.find('7')+1)])
print(email[email.find('.'):])
print(email.find('i'))
print(email.find('i', 2, 13)) # string.find(value, start, end)
print(email.index('t'))
print(email.index('t', 10, 20)) # string.index(value, start, end)
print(email.count('i'))
print(email.count('i',0,9)) # string.count(substring, start=..., end=...)
print(email.replace('07', '007'))
print(email.replace('a', 'A'))
print(email.replace('a', 'A', 1)) # string.replace(oldvalue, newvalue, count)
print(email)
print("\n")

first_name = 'Vasudev'
last_name  = 'Bonu'
age = 27

print('My name is %s and I am %d years old.' %(first_name, age)) # String interpolation
print(f"Hi Python Lovers! My name is {last_name} {first_name}.")
message = "Hello Python Lovers! My name is {} {}.".format(last_name, first_name)
print(message)

person = {'name': 'deva', 'age': 27}
sentence = 'My name is {} and I am {} years old.'.format(person['name'].upper(), person['age'])
print(sentence)
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'].title(), person['age'])
print(sentence)
sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
print(sentence)
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

l = ['vasu', 27]
sentence = 'My name is {0[0]} and I am {0[1]} years old'.format(l)
print(sentence)


tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)


class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person('tiru', 27)

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)


sentence = 'My name is {name} and I am {age} years old.'.format(name='vasudev', age=27)
print(sentence)


# format numbers
for i in range(1,11):
    sentence = 'The value is {:03}'.format(i)
    print(sentence)
print("\n")

import math
print(math.pi)

sentence = 'Pi is equal to {:.2f}'.format(math.pi)
print(sentence)

sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)
print("\n")

# format date
import datetime
my_date = datetime.datetime(2020, 4, 2, 14, 30)
print(my_date)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# day of 1947 aug 15th
import datetime
mydate = datetime.datetime(1947, 8, 15, 12)
print(mydate)
sentence = '{0:%B %d, %Y} is {0:%A} and was the {0:%j} day of the year.'.format(mydate)
print(sentence)


print("\n")

name = ' vasudev '
print(name)
print(len(name))
print(f"{name.rstrip()}: {len(name.rstrip())}")
print(f"{name.lstrip()}: {len(name.lstrip())}")
print(f"{name.strip()}: {len(name.strip())}")
print("\n")

name = 'tirupathinaidu'
print(len(name))
print(name.index('i'))
print(name[0])
print(name[-1])
print(name[::-1]) # reverse
print("\n")

url = 'https://coreyms.com'
print(url[(url.find('/')+2):])
print(url[(url.find('/')+2):url.find('.')])
print("\n")

message = f"\tHello\n\tPython\n\tLovers!"
print(message)
print("\n")

memento = 'I can\'t remember to forget you!'
print(f"{memento}\n")



# Numbers
# int
num = 3
print(type(num))
print("\n")

# float
num = 3.14
print(type(num))
print("\n")

# imaginary
z = 2+3j
print(z)
print(type(z))
print(z.real)
print(z.imag)
print("\n")

# math operation
print("Math")
print(2 + 3)
print(4 - 2)
print(5 * 2)
print(8 / 4)
print(10 % 2)
print(6 // 2) # floor division
print(7 // 2) # floor division
print(2 ** 8)
print("\n")

# Print function - Sep(seperator) parameter
print("There are <", 2**32, "> possibilities!", sep="")
print('deva07','gamil.com', sep="@")
print("\n")

# Print function end parameter
for x in range(1,11):
    print(x, end=' ')
print("\n")


# BIDMAS
print("BIDMAS")
print(4 + 5 * 2)
print((4+5) * 2)
print("\n")


# Underscore in numbers 
print("Underscore in numbers")
universe_age = 14_000_000_000
print(universe_age)
print("{:,.2f}".format(100_000_000_00))
print(f"{10000000000:,.2f}")
print("\n")


# Multiple assignment
print("Multiple assignment")
x, y, z = 1, 2, 3
print(x, y, z)
print("\n")


num = 1
num += 1
print(num)
# print(dir(num))
# print(help(int))
print("\n")

num = -3
print(abs(num))
num = 3.75
print(round(num))
print(round(num,1))
print("\n")

num_1 = "100"
num_2 = "200"
print(num_1 + num_2)
print(int(num_1) + int(num_2)) # Casting
print("\n")



# Lists
print("Lists")
number = 1345234156
print(f"{number}")
print(str(number))
print(f"List: {list(str(number))}")
print("\n")

numbers = [2, 6, 1, 3, 4, 7, 9]
print(numbers.index(3))
print(numbers[::-1])
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print("\n")

numbers = [1, 2, 2, 2, 3, 3, 5, 6, 7, 4, 4, 8, 4, 9, 4, 1, 9, 4, 5, 3, 2, 1, 1, 9, 5, 8, 3, 2, 3, 7, 6, 5, 8, 7, 8, 2, 1, 1, 9, 5, 8, 3, 2, 3, 7, 6, 4, 1, 1, 2, 5, 6, 4, 9, 8]
print(max(numbers))
print(min(numbers))
print(max(set(numbers), key = numbers.count))
print("\n")

numbers = [2, 2, 1, 1, 3, 3, 6, 6, 7, 7, 8, 8, 2, 6]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
print(max(set(numbers), key=numbers.count))
print(max(set(numbers), key=lambda value: numbers.count(value)))

for i in range(len(numbers)):
    number = max(set(numbers), key=numbers.count)
    print(number, numbers.count(number))
    if numbers.count(number) == 1:
        break
    numbers.remove(number)

print('\n')

# Slicing
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9 
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

print(my_list[0])
print(my_list[9])
print(my_list[-1])
print(my_list[1:])
print(my_list[2:-1:2])
print(my_list[-2:1:-1])
print(my_list[::1])
print(my_list[::-1])
print("\n")

name = 'tirupathinaidu'
print(name[0:4])
print(name[::-1])
print(name[-5:])
print("\n")


names = ['ching', 'chang','chung', 'ding', 'dang',]
print(names)
print(len(names))
print(names.index('ding'))
print('ding' in names)
print(names[1])
print(names[2:5])
print(names[-2])
print(names[-3:])
print(names[::-1]) #reverse order
print("\n")


# add items

names.extend(['pong'])
print(names)
print("\n")

names.append('ping')
print(names)
print("\n")

names.insert(2, 'bing')
print(names)
print("\n")

# Change items
names[2] = 'bang'
print(names)
print("\n")

# remove items
item_1 = names.pop(2)
print(item_1)
print(names)

del names[-1]
print(names)

names.remove('pong')
print(names)
print("\n")

# Sorted - temporary
print(names)
print(sorted(names))
print(sorted(names, reverse = True))
print(names)
print("\n")

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)
print("\n")

py_list = ['ejkajd', 'ahj', 'uhafkjhafjnajdbjk', 'oajfafyad', 'ioiqworjqifhh']
print(sorted(py_list, key=len))
print("\n")

strs = ['aa', 'BB', 'zz', 'CC']
print('B'<'a')
print(sorted(strs))
print(sorted(strs, key=str.lower))
print("\n")

# reverse
print(names)
names.reverse()
print(names)
names.reverse()
print(names)
print("\n")

# sort - permanent
print(names)
names.sort()
print(names)
names.sort(reverse = True)
print(names)
print("\n")

def sortSecond(val):
    return val[1]
list1 = [(1,2), (3,3), (1,1)]
list1.sort(key = sortSecond)
print(list1)

list1.sort(key = sortSecond, reverse=True)
print(list1)
print("\n")

strs = ['xc', 'zb', 'yd' ,'wa']

def MyFn(s):
    return s[-1]

print(MyFn(strs))

print(sorted(strs, key=lambda value: value[-1]))
print("\n")


letters = {
    'D':4,
    'A':1,
    'P':16,
    'B':2
}
print(sorted(letters))
print("\n")

letters = {
    4:'D',
    1:'A',
    16:'P',
    2:'B'
}
print(sorted(letters))
print("\n")

# for loop
names = ['ching', 'chang','chung', 'ding', 'dang']
for name in names:
    print(name)

print("\n")


for value in range(1, 5):
    print(value)

print("\n")


numbers = list(range(1, 6))
print(numbers)

print("\n")


squares = []
for number in range (1, 11):
    square = number ** 2
    squares.append(square)
print(squares)

print("\n")


# list comprehensions
squares = [number**2 for number in range(1, 11)]
print(squares)

print("\n")


# for loop - enumerate function
for index, name in enumerate(names):
    print(f"Index {index}: {name}")

print("\n")

# for loop - enumerate function, start value
for index, name in enumerate(names, start = 1):
    print(f"Index {index}: {name}")

print("\n")

# join method - its a string method
# list to string
name_str = ' - '.join(names)
print(name_str)

# string to list
new_list = name_str.split(' - ')
print(new_list)


# copying a list using slice
names_1 = ['ching', 'chang', 'chung']
copy_names_1 = names_1[:]
print(copy_names_1)
copy_names_1.append('chong')
print(copy_names_1)
print(names_1)
print("\n")

copy_names_1 = names_1
print(copy_names_1)
copy_names_1.append('chong')
print(copy_names_1)
print(names_1)
print("\n")

toppings = ['pepper', 'mushroom', 'onions']
toppings1 = toppings.copy()
print(id(toppings))
print(id(toppings1))
toppings.append('chilli pepper')
print(toppings)
print(toppings1)
print("\n")


# Tuples - Immutable

# Mutable
list_1 = ['history', 'math', 'physics', 'compsci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'art'

print(list_1)
print(list_2)

print("\n")

# Immutable
tuple_1 = ('history', 'math', 'physics', 'compsci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'art'

# print(tuple_1)
# print(tuple_2)

print("\n")


# Tuples are technically defined by the presence of a comma
values = (1)
print(values, type(values))
print(values + 3)
values = (1,)
print(values, type(values))

print("\n")



# Sets - set are values that are unordered and also have no duplicates
cs_courses = {'history', 'math', 'physics', 'compsci'}
print(cs_courses)

# Sets - remove duplicates
cs_courses = {'physics', 'history', 'math', 'physics', 'compsci', 'math'}
print(cs_courses)

# Sets - membership test
print('math' in cs_courses) # This can be done with lists and tuples but sets are optimized for this.

# Sets - intersection, difference, union methods
cs_courses = {'history', 'math', 'physics', 'compsci'}
art_courses = {'history', 'math', 'art', 'design'}
print(cs_courses.intersection(art_courses))
print(cs_courses & art_courses)

print(cs_courses.difference(art_courses))
print(cs_courses - art_courses)

print(art_courses.difference(cs_courses))
print(art_courses - cs_courses)

print(cs_courses.union(art_courses))
print(cs_courses | art_courses)

print(cs_courses ^ art_courses)
print(cs_courses.symmetric_difference(art_courses))

print("\n")


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_list = ()
empty_list = tuple()

# Empty Sets
empty_list = {} # This isn't right! it's a dict
empty_list = set()


print("\n")


# Dictionaries - working with key-value pairs
student = {
    'name': 'deva',
    'age': 27,
    'courses': ['math', 'python'],
}

print(student['name'])

# student['name'] = 'vasu'
# student['phone'] = '555-55556'
# print(student.get('phone', 'Not Found'))

# update multiple things at a time - update method
# student.update({'name': 'vasu', 'age': 26, 'phone': '555-55556'})

# print(student)


# delete key-value

# del student ['age']
# print(student)

age = student.pop('age')
print(age)
print(student)

print("\n")


# Loop through dictionaries - for loop
student = {
    'name': 'deva',
    'age': 27,
    'courses': ['math', 'python'],
}

print(len(student))
print(student.items())
print(student.keys())
print(student.values())

print("\n")


for key, value in student.items():
    print(key, value)
print("\n")


person = {
    'name': 'vasu',
    'age': 27,
    'hobbies': ['chess', 'drawing', 'reading'],
    'address': {
        'street': 'chocolate factory road',
        'city': 'bangalore',
        'state': 'karnataka',
        'pincode': 530068
    },
    'favorite': [{'food': 'dosa'}, 
    {'cricket': 'sachin','tennis':'roger federer'}]

}

for x in person['favorite']:
    for key, value in x.items():
        print(key.title(), value, sep=" - ")
print("\n")


# Conditionals and Booleans - if,elif,else
# Comparisons
# Equal: ==
# Not Equal: !=
# Greater Than: >
# Less Than: <
# Greater or Equal: >=
# Less or Equal: <=
# Object Identity: is

print(10 > 3)
print(10 >= 3)
print(10 < 20)
print(10 <= 20)
print(10 == 10)
print(10 == "10")
print(10 != "10")

print("bag" > "apple")
print("bag" > "BAG")
print("bag" == "BAG")
print(ord("b"))
print(ord("B"))
print("\n")

language = 'python'

if language == 'python':
    print("Condition was true")

if 'p' in language:
    print("Hello Python Lovers!")

if 'l' not in language:
    print("Hello All!")


language = 'JavaScript'

if language == 'python':
    print("Language is python")
elif language == 'JavaScript':
    print("Language is JavsScript")
else:
    print("No Match")

print("\n")

# Logical operators and, or & not
user = 'Admin'
loggned_in = True

if user == 'Admin' and loggned_in:
    print("Admin page")
else:
    print("Bad creds")


user = 'Admin'
loggned_in = False

if user == 'Admin' or loggned_in:
    print("Admin page")
else:
    print("Bad creds")


user = 'Admin'
loggned_in = False

if not loggned_in:
    print("Admin page")
else:
    print("Bad creds")

print("\n")


# Object Identity: is
a = [1,2,3]
b = [1,2,3]
print(a == b)

print(id(a))
print(id(b))
print(a is b) # Here a and b objects are different in memory.

a = [1,2,3]
b = a
print(a == b)

print(id(a))
print(id(b))
print(a is b)

print("\n")



# False values
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping or empty dictionary. For example, {}.

condition = False

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

print("\n")


# Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

print("\n")


# Loops and Iterations - For/While Loops
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)
print("\n")


# break statement
for num in nums:
    if num == 3:
        print("Found!")
        break
    print(num)

print("\n")


# continue statement
for num in nums:
    if num == 3:
        print("Found!")
        continue
    print(num)

print("\n")


# loop within a loop
nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)
    print("\n")


# range
for i in range(1, 11):
    print(i)
print("\n")


# While loops
x = 0

while x < 10:
    print(x)
    x += 1
print("\n")



# Python Built-in functions
# abs() - absolute value
print(abs(-9))
print(abs(5))
print(abs(0))
print("\n")

# bool()
print(bool(""))
print(bool(" "))
print(bool(3))
print(bool("t"))
print(bool(-4))
print(bool(None))
print(bool(0))
print("\n")

''' The difference between the two is that eval
returns a value (something that you can save in a variable), whereas exec does not.'''

# eval() - evaluate
print(eval("34*74"))
eval('print("wow")')
cal = eval(input("Enter a calculation: "))
print(cal)

# exec()
my_small_program = '''print('ham')
print('sandwich')'''
exec(my_small_program)

# creating a test file
test_file = open(r'C:\Users\vasudev\Desktop\hello\hi.txt')
read_file = test_file.read()
print(read_file)

test_file_1 = open(r'C:\Users\vasudev\Desktop\hello\hola.txt', 'w')
test_file_1.write("The Law of Life is the Law of Belief.")

test_file_1 = open(r'C:\Users\vasudev\Desktop\hello\hola.txt')
read = test_file_1.read()
print(read)
test_file_1.close()


# Useful python modules

# Making Copies with the copy Module
import copy

class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color

# harry = Animal('hippogriff', 6, 'pink')

# harriet = copy.copy(harry)

# print(harriet.species)

harry = Animal('hippogriff', 6, 'pink')
carrie = Animal('chimera', 4, 'green polka dots')
billy = Animal('bogill', 0, 'pasley')

# copy.copy(list)
# my_animals = [harry, carrie, billy]
# more_animals = copy.copy(my_animals)

# # print(more_animals[1].species)
# # print(my_animals[0].species)

# my_animals[0].species = 'ghoul'
# print(my_animals[0].species)
# print(more_animals[0].species)
# print(id(my_animals[0]))
# print(id(more_animals[0]))

# copy.deepcopy(list)
my_animals = [harry, carrie, billy]
more_animals = copy.deepcopy(my_animals)

# print(more_animals[1].species)
# print(my_animals[0].species)

my_animals[0].species = 'ghoul'
print(my_animals[0].species)
print(more_animals[0].species)
print(id(my_animals[0]))
print(id(more_animals[0]))


# Keep track of keywords with the keyword module
import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('hi'))
print(keyword.kwlist)


# random module
# Guessing number
import random
num = random.randint(1, 100)

while True:
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
        print("You guessed right")
        break
    elif i < num:
        print("Try higher")
    elif i > num:
        print("Try lower")

# Using choice to pick a randoom item from a list
import random
desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']

print(random.choice(desserts))

# Using shuffle to shuffle a list
import random
desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']

random.shuffle(desserts)
print(desserts)

# Controlling the shell with the sys module
import sys
sys.exit()

# Reading with the stdin object
import sys

print("What's your age? ")
message = int(sys.stdin.readline())

if message < 10:
    print("Hey kid!")
elif message >= 10 and message < 30:
    print('Ho!! Boy!')
else:
    print("Ho! Man!")

# Writing with the stdout object
import sys
sys.stdout.write("What does a fish say when it swims into a wall? Dam.\n")
message = sys.stdout.write("What does a fish say when it swims into a wall? Dam.")
print(message)

# time module
import time
print(time.localtime()) # returns the current date and time as an object
print(time.localtime()[0])
print(time.asctime()) # takes a date as a tuple

# sleep()
import time
for num in range(1, 21):
    print(num)
    time.sleep(1)

# Using the pickle module to save information
import pickle

game_data = {
    'player_position': 'N23 E45',
    'pockets': ['keys', 'pocket knife', 'polished stone'],
    'backpack': ['rope', 'hammer', 'apple'],
    'money': 158.50
}

save_file = open(r'C:\Users\vasudev\Desktop\save.dat', 'wb')

pickle.dump(game_data, save_file)
save_file.close()

load_file = open(r'C:\Users\vasudev\Desktop\save.dat', 'rb')

loaded_game_data = pickle.load(load_file)
load_file.close()



# Python Tips and Tricks 
# Ternary Conditionals
condition = True
x = 1 if condition else 0
print(x)
print("\n")


# Underscore Placeholders
number1 = 10_000_000_000
number2 = 10_000_000
total = number1 + number2
print(f'{total:,.3f}')
print("\n")


# Enumerate
names = ['ching', 'chang', 'chung', 'ding']
for index, name in enumerate(names, start = 1):
    print(index, name.title())
print("\n")


# Zip
names = ['ching', 'chang', 'chung', 'ding']
heroes = ['spiderman', 'superman', 'deadpool', 'batman']
universes = ['marvel', 'DC', 'marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name.title()} is actually {hero.title()} from {universe.title()}')
print("\n")

for value in zip(names, heroes, universes):
    print(value)
    print(type(value))
print("\n")


# Unpacking
# a, b = (1, 2)
# print(a)
# print(b)

# a, _ = (1, 2)
# print(a)

# a, b, *c = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)

# a, b, *_ = (1, 2, 3, 4, 5)
# print(a)
# print(b)

a, b, *c, d = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
print(d)
print("\n")


# List Comprehensions

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [n for n in range(1,11)]
print(my_list)
my_list = list(map(lambda n: n, range(1,11)))
print(my_list)
print("\n")

my_list = [n*n for n in range(1,11)]
print(my_list)
my_list = list(map(lambda n: n*n, range(1,11)))
print(my_list)
print("\n")

my_list = [n for n in range(1,11) if n%2 == 0]
print(my_list)
my_list = list(filter(lambda n: n%2 == 0, range(1,11)))
print(my_list)
print("\n")

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)
print("\n")


# Dictionary Comprehensions

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)
print("\n")
print(dict(zip(names, heros)))
print("\n")
print(list(zip(names, heros)))
print("\n")
print(set(zip(names, heros)))
print("\n")
print(tuple(zip(names, heros)))
print("\n")


# Set Comprehensions

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]

my_set = {n for n in nums}
print(my_set)
print("\n")


# Generator Expressions
# I want to yield 'n*n' for each 'n' in terms

nums = [1,2,3,4,5,6,7,8,9,10]
# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# for i in my_gen:
#     print (i)

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
print("\n")


# Functions

# def hello_func():
#     pass

# hello_func()

name = 'deva'

def hello_func():
    return f"Hello {name.title()}"

print(hello_func())
print(hello_func())
print(hello_func())
print(hello_func())

