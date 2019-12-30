# Changing, Adding and Removing Elements

# Modifying Elements in a List
print("\n\n\n")
print("Modifying Elements in a List")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)


# Adding Elements to a List
print("\n\n\n")
print("Adding Elements to a List")
motorcycles.append('honda')
print(motorcycles)

# Using an empty list
print("\n\n\n")
print("Using an empty list")
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


# Inserting Elements into a List
print("\n\n\n")
print("Inserting Elements into a List")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)


# Removing Elemets from a list
# Removing an item using the del statement
print("\n\n\n")
print("Removing an item using the del statement")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)


# Removing an item using the pop() method
print("\n\n\n")
print("Removing an item using the pop() method")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}")


# Remove an item by value
print("\n\n\n")
print("Remove an item by value")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")



# Organizing a List
print("\n\n\n")
print("Organizing a List")
cars = ['bmw','audi', 'toyota', 'subaru']
print(cars)

# Sorting a List Permanently with the sort() method
print("\n\n\n")
cars = ['bmw','audi', 'toyota', 'subaru']
cars.sort() # alphabetical order and we never revert to the original order
print(cars)

# reverse alphabetical order
cars.sort(reverse = True) # the order of the list is permanently changed
print(cars)

# Sorting a List Temporarily with the sorted() function
print("\n\n\n")
cars = ['bmw','audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# alphabetical order - Temporary
print(sorted(cars))
# reverse alphabetical order - Temporary
print(sorted(cars, reverse = True))


# Printing a List in Reverse Order
print("\n\n\n")
cars = ['bmw','audi', 'toyota', 'subaru']
print(cars)
cars.reverse() # This method changes the order of a list permanently
print(cars)


# Finding the Length of a List
print("\n\n\n")
cars = ['bmw','audi', 'toyota', 'subaru']
print(len(cars))
