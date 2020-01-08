# Python Crash Course

"""Hello 
Python 
Lovers!"""

# String

print("Hello Python Lovers!")

email = "tirupathinaidu07@gmail.com"

# print(dir(email))
# print(help(str))
print(help(str.lower))

print(email)
print(email.upper())
print(email.lower())
print(email.title())
print(email.capitalize())
print(email.count('i'))
print(email.find('i'))
print(email.replace('07', '007'))
print(email)
print("\n")

first_name = 'Vasudev'
last_name  = 'Bonu'

print(f"Hi Python Lovers! My name is {last_name} {first_name}.")
message = "Hello Python Lovers! My name is {} {}.".format(last_name, first_name)
print(message)

person = {'name': 'deva', 'age': 27}
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'].title(), person['age'])
print(sentence)
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
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
print("\n")

message = f"\tHello\n\tPython\n\tLovers!"
print(message)
print("\n")

memento = 'I can\'t remember to forget you!'
print(f"{memento}\n")



# Numbers
num = 3
print(type(num))

num = 3.14
print(type(num))
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

# BIDMAS
print("BIDMAS")
print(4 + 5 * 2)
print((4+5) * 2)
print("\n")


# Underscore in numbers 
print("Underscore in numbers")
universe_age = 14_000_000_000
print(universe_age)
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
print(int(num_1) + int(num_2))
print("\n")



# Lists
print("Lists")
number = 1345234156
print(f"{number}")
print(str(number))
print(f"List: {list(str(number))}")
print("\n")

numbers = [2, 6, 1, 3, 4, 7, 9]
print(numbers[::-1])
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print("\n")


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




# collection_list = []
# for number in range(1, 1000):
#     fraction = 1/number
#     list_str = list(str(fraction))
#     collection_list.append(list_str)

# min_list_len = []
# for min_list in collection_list:
#     min_list_len.append(len(min_list[2:]))
#     y = set([x for x in min_list if min_list.count(x)>1])

# print(y)

# print((min_list_len))
# print(min_list_len.index(21))

# import math

# for x in range(1, 401):
#     for y in range(1, 401):
#         for z in range(1, 401):
#             if (x + y == math.sqrt(x+y) and x - y == math.sqrt(x-y) and x + z == math.sqrt(x+z) and x - z == math.sqrt(x-z) and y + z == math.sqrt(y+z) and y - z == math.sqrt(y-z)):
#                 print(x + y + z)

# import math

# for x in range(1, 10001):
#     for y in range(1, 10001):
#         if (x + y == math.sqrt(x+y) and x - y == math.sqrt(x-y)):
#             print(x + y)


# numbers = [7,2,3,4,1,4,5,6,7,8,9,2]

# without_duplicatenumbers = []

# for number in numbers:
#     if numbers.count(number)>1:
#         without_duplicatenumbers.append(number)

# print(set(without_duplicatenumbers))

# print("\n")


# name = 'vasudevatirupathinaiduvasudevatirupathinaidu'

# print(name.count('i'))

