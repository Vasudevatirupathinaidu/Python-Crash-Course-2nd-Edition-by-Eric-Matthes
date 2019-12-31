# Making Numerical Lists
# Using a range() function
for value in range(1, 6):
	print(value)
print("\n")

for value in range(6):
	print(value)
print("\n")

for value in range(1, 12, 2): # 3rd argument '2' is a step size
	print(value)
print("\n")

for value in range(2, 12, 2): # 3rd argument '2' is a step size
	print(value)
print("\n")


# Using range() to make a list of numbers
numbers = list(range(1, 6))
print(numbers)
print("\n")


# Simple statistics with a list of numbers
digits = list(range(10))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))