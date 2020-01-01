# Tuples
# Defining a Tuple - A list of items that cannot change(Immutable).
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 - 'tuple' object does not support item assignment

# Tuples are technically defined by the presence of a comma; you need to include a trailing comma
my_t = (3,)
print(my_t)
print("\n")


# Looping through all values in a tuple
dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)
print("\n")


# Writing over a tuple - redefine the entire tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)


dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)