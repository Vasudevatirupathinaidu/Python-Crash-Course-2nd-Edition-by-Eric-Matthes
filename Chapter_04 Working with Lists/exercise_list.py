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
# 	print(number)

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