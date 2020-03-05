# Reading an Entire file
'''open() function returns an object representing the file.
The keyword 'with' closes the file once access to it is no longer needed.'''
with open('text_files/pi_digits.txt') as file_object:
	contents = file_object.read()
	# print(contents.rstrip())
print(contents)
print("\n")

# Old approch
# file = open('pi_digits.txt')
# print(file.read())
# file.close()


# Reading line by line
filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line)
		# print(line.rstrip())
print("\n")


# Making a list of lines from a file
filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

print(lines)
for line in lines:
	print(line.rstrip())