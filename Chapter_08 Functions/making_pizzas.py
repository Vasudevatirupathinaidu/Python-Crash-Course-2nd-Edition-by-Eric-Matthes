# Storing Your Functions in Modules

# Importing an Entire Module - module_name.function_name()
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n")


# Importing Specific Function - from module_name import function_name (or) from module_name import function_0, function_1, function_2

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n")


# Using as to Give a Function an Alias - from module_name import function_name as fn . (The as keyword renames a function using the alias you provide)

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n")


# Using as to Give a Module an Alias - import module_name as mn
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n")


# Importing All Functions in a Module - from module_name import *
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n")