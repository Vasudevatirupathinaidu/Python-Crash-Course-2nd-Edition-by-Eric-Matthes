# Working with a file's contents

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

print(lines)
print("\n")

pi_string = ''
for line in lines:
	pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
print("\n")

list_of_lines = [line.rstrip() for line in lines]
print(''.join(list_of_lines))
print("\n")


# Large files: one million digits
filepath = 'text_files/pi_million_digits.txt'

with open(filepath) as file_object:
	contents = file_object.read()

print(f"{contents[:52]}....")


# Is Your Birthday Contained in Pi?

filepath = 'text_files/pi_million_digits.txt'

with open(filepath) as file_object:
	lines = file_object.readlines()

list_of_lines = [line.strip() for line in lines]

pi_string = ''.join(list_of_lines)

birthday = input("Enter your birthday, in the form of ddmmyy: ")

if birthday in pi_string:
	print("Your birthday appears in the first millon digits of pi!")
	print(f"Index: {pi_string.index(birthday)}")
else:
	print('Your birthday does not appears in the first millon digits of pi.')