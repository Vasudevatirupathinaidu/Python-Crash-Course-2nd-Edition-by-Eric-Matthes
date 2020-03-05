# Writing to a file
# Writing to an empty file
filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.")

# Writing multiple lines
filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")


# Appending to a file
filename = "text_files/programming.txt"

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
