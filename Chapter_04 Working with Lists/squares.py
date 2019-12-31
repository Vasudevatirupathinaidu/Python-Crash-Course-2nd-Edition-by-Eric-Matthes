squares = []
for value in range(1, 11):
	square = value**2
	squares.append(square)
print(squares)
print("\n")

# List Comprehensions - A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.

squares = [value**2 for value in range(1, 11)]
print(squares)