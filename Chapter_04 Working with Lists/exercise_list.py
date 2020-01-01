# Pizzas
pizzas = ['chicago pizza', 'greek pizza', 'detroit pizza']
print(pizzas)
for pizza in pizzas:
    print(f"I like {pizza.title()}!")
print("I really love Pizza!")
print("\n")

# Animals
animals = ['lion', 'monkey', 'zebra']
for animal in animals:
    print(f"Be like a {animal.title()}")
print("The animals are part of an ecosystem.")
print("\n")


# Counting to twenty
for value in range(1, 21):
    print(value)
print("\n")


# One million
numbers = list(range(1, 1000001))
# print(numbers)
# for number in numbers:
#   print(number)

# Summing a million
numbers = list(range(1, 1000001))
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))


# Odd numbers
for value in range(1, 20, 2):
    print(value)
print("\n")


# Threes
# method 1
threes = []
for value in range (1, 11):
    number = value*3
    threes.append(number)
print(threes)
print("\n")

# method 2 - List Comprehension
threes = [value*3 for value in range(1, 11)]
print(threes)
print("\n")

# Cubes
# method 1
cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
print(cubes)
print("\n")

# method 2 - List Comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)
print("\n")



# Slices
nolan_movies = ['Memento', 'The Prestige', 'Inception', 'The Dark Knight', 'Interstellar', 'TENET']
print("The first three items in the list are:")
print(nolan_movies[:3])

print("\nThree items from the middle of the list are:")
print(nolan_movies[1:4])

print("\nThe last three items in the list are:")
print(nolan_movies[-3:])

print("\n")


# My pizzas, your pizzas
my_pizzas = ['chicago pizza', 'greek pizza', 'detroit pizza']
friend_pizzas = pizzas[:]
print(my_pizzas)
print(friend_pizzas)
my_pizzas.append('california pizza')
friend_pizzas.append('sicilian pizza')

print("\n")
print(my_pizzas)
print(friend_pizzas)

print("\n")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
print("\n")


# Buffet
food_items = ('chicken biryani', 'dal rice', 'curd rice', 'lachha paratha', 'paneer')
for item in food_items:
    print(item)
print("\n")


# modify one of the items
# food_items[1] = 'dal fry' - 'tuple' object does not support item assignment
# print(food_items)
food_items = ('chicken biryani', 'dal fry', 'khichdi', 'lachha paratha', 'paneer')
for item in food_items:
    print(item)



# Converting Tabs to Spaces - If you use a mix of tabs and spaces in your code, it can cause problems in your programs that are difficult to diagnose. To avoid this, you can configure Sublime Text to always use spaces for indentation, even when you press the tab key. Go to View -> Indentation and make sure the Indent Using Spaces option is selected. If it’s not, select it. Also, make sure the Tab Width is set to 4 spaces.

# PEP 8 (Python Enhancement Proposal) https://www.python.org/dev/peps/pep-0008/