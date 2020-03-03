# print(dir())
# print(dir(__builtins__))
print("\n")

help(pow)
print("\n")

# hexadecimal
help(hex)
print(hex(10))
print(0Xa)
print("\n")

# help('modules') # list of available modules
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
-method: strptime()
'''
moon_landing = "7/20/1969"
moon_landing = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing)
print(type(moon_landing))
print("\n")

help(datetime.datetime.strptime)
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
tuple_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
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

# Logging in Python
