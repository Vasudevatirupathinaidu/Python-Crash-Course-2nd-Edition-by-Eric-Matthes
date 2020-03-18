
import sys,os
print(sys.executable)
print("\n")
print(sys.path)
print("\n")
print(sys.path[0])
print("\n")
print(os.listdir())
print("\n")
print(os.path)
print("\n")
print(os.getcwd())
print("\n")
print(os.__file__)
print("\n")


# print(dir())
# print(dir(__builtins__))
print("\n")

# help('modules') # list of available modules
print("\n")

# Python Errors and Built-in Exceptions
# errors = locals()['__builtins__']
# print(dir(errors))


help(pow)
print("\n")


# Arithmetic +, -, * and /
'''ints are narrower than floats
floats are wider than ints'''
x = 28
print(float(x))
y = 3.14
print(int(y))
print("\n")

'''floats are narrower than complex numbers
complex numbers are wider than floats
'''
x = 1.732
print(complex(x))
y = 1.732 + 0j
# print(float(y)) # It causes error
print("\n")


# hexadecimal
help(hex)
print(hex(10))
print(0Xa)
print("\n")


import math
print(dir(math))
help(math.radians)
print(math.radians(180))
print("\n")

from math import radians
print(radians(180))
print("\n")


# Boolean Conversation
''' trivial -> False
    non-trivial -> True '''
print(str(True))
print(str(False))
print(int(True))
print(int(False))
print(5 + True)
print(10 * False)
print("\n")


# Datetime module
import datetime
print(dir(datetime))
help(datetime.date)
gvr = datetime.date(1956, 1, 31)
print(gvr)
print(type(gvr))
print(gvr.year)
print(gvr.month)
print(gvr.day)
print("\n")

mill = datetime.date(2000, 1, 1)
print(mill)
dt = datetime.timedelta(100)
print(dt)
print(mill + dt)
print("\n")

# Day-name, Month-name Day-#, Year
print(gvr.strftime("%A, %B %d, %Y"))
message = "GVD was born on {:%A, %B %d, %Y}"
print(message.format(gvr))
print("\n")

# date, time, datetime
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date)
print(launch_time)
print(launch_datetime)
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)
print("\n")


# Access current datetime
'''
-module: datetime
-class: datetime
-method: today()
'''
now = datetime.datetime.today()
print(now)
print(now.microsecond)
print("\n")

# Convert string to datetime
'''
-module: datetime
-class: datetime
-method: strptime() -->sringpasstime
'''
moon_landing = "7/20/1969"
moon_landing = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing)
print(type(moon_landing))
print("\n")

help(datetime.datetime.strptime)
print("\n")


# Calendar
import calendar
print(calendar.isleap(2020))
print(calendar.isleap(2017))
print("\n")

# Sets
example = set()
print(dir(example))
example.add(False)
example.add(42)
example.add(3.14159)
example.add("Nitrogen")
print(example)
print(len(example))
example.remove(42)
print(len(example))

# example.remove(50) # To avoid the possibility of an error, there is a second way to remove an element i.e discard

example.discard(50) # do nothing
print("\n")

# Tuples
'''Lists occupy more memory than tuples''' 
import sys
print(dir(sys))
help(sys.getsizeof) # It will tell you the size of an object in bytes
list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))
print("\n")

# Tuples can be made more quickly than lists
import timeit
list_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print("List time = ", list_test)
print("Tuple time = ", tuple_test)
print("\n")

# Tuple assignment
age, country, knows_python = 27, 'india', True
print(age, country, knows_python)
print("\n")

# Unpacking
a, b, *c = 1, 2, 3, 4
print(c)

x, y, *_ = 1, 2
print("\n")


# List Comprehensions

remainders = [x**2 % 5 for x in range(1,101)]
print(remainders)
print("\n")


letters = [('b',2), ('d',4), ('a',1), ('c',3), ('e',5), ('f',6)]
list_copr = [letter for (letter,number) in letters if number >= 3]
print(list_copr)
print("\n")

# Cartesian Product
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(x,y) for x in A for y in B]
print(cartesian_product)



# JSON
'''
json.load(f): Load JSON data from file(or file-like object)
json.loads(s): Load JSON data from a string
json.dump(j, f): Write JSON object to file (or file-like object)
json.dumps(j): Output JSON object as string
'''
import json
print(dir(json))
print("\n")

# json.loads example
value = """
    {"title": "Sigma",
    "release_year": 2020,
    "actors": null,
    "won_oscar": false
    }"""

sigma = json.loads(value)
print(sigma)
print("\n")

# json.dumps example
movie = {'title': 'Inception', 'release_year': 2010, 'is_awesome': True, 'won_oscar': False, 'budget': None, 'bigfan': 'Łatynka'}

inception = json.dumps(movie, ensure_ascii=False)
print(inception)
print("\n")


# Lambda Expressions & Anonymous Functions
# Write function to compute 3x+1
def f(x):
    return 3*x + 1

result = f(2)
print(result)

result2 = lambda x: 3*x + 1
print(result2(3))
print("\n")

# Combine first name and last name into a single "Full Name"
full_name = lambda fn, ln: f"{fn.strip().title()} {ln.strip().title()}"
print(full_name(" leonardo", "da vinci"))
print("\n")

# Lambda Expressions
''' lambda <inputs>: <expression> '''

# A function with no name
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "Leigh Brackett"]

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)
print("\n")

# A function that makes functions
def build_quadratic_function(a, b, c):
    """Return the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

print(build_quadratic_function(2, 3, 4)(2))
print("\n")


# Map, Filter, and Reduce Functions
import math

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method
areas = []
for r in radii:
    a = area(r)
    areas.append(a)
print(areas)

# Method 2: Use 'map' function
print(list(map(area, radii)))
print("\n")

# celcius to farenheit
temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28), ("London", 22)]
c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

print(list(map(c_to_f, temps)))
print("\n")


# Filter Function
import statistics
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)
print("\n")

print(list(filter(lambda x: x > avg, data)))
print(list(filter(lambda x: x < avg, data)))
print("\n")

# Remove missing data
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuela"]
print(list(filter(None, countries)))
print("\n")


# Reduce Fumction
# Multiply all numbers in a list
from functools import reduce
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print(reduce(lambda x,y: x*y, data))

# Direct method
product = 1
for x in data:
    product = x * product
print(product)
print("\n")


# Text Files in Python
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
with open("c:/users/vasudev/Desktop/test.txt", 'w') as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")