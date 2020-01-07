# Python Crash Course

"""Hello 
Python 
Lovers!"""

# String

print("Hello Python Lovers!")

email = "tirupathinaidu07@gmail.com"
print(email)
print(email.upper())
print(email.lower())
print(email.title())

first_name = 'Vasudev'
last_name  = 'Bonu'
print(f"Hi Python Lovers! My name is {last_name} {first_name}.")
message = "Hello Python Lovers! My name is {} {}.".format(last_name, first_name)
print(message)

name = ' vasudev '
print(name)
print(len(name))
print(f"{name.rstrip()}: {len(name.rstrip())}")
print(f"{name.lstrip()}: {len(name.lstrip())}")
print(f"{name.strip()}: {len(name.strip())}")

name = 'tirupathinaidu'
print(name[0])
print(name[0:4])
print(name[::-1])

message = f"\tHello\n\tPython\n\tLovers!"
print(message)

memento = 'I can\'t remember to forget you!'
print(f"{memento}\n")


# Numbers

# math operation
print("Math")
print(2 + 3)
print(4 - 2)
print(5 * 2)
print(8 / 4)
print(10 % 2)
print(6 // 2)
print(7 // 2) #floor
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


# Lists
print("Lists")
number = 1345234156
print(f"{number}")
print(str(number))
print(f"List: {list(str(number))}")














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

