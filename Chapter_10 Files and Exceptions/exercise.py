# Learning Python
filename = 'text_files/learning_python.txt'

with open(filename) as file_object:
	content = file_object.read()

print(content)
print("\n")


with open(filename) as file_object:
	for line in file_object:
		print(line.strip())
print("\n")


with open(filename) as file_object:
	lines = file_object.readlines()

print(lines)
for line in lines:
	print(line.strip())
print("\n")


# Learning C

filename = 'text_files/learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	if 'python' in line:
		line = line.strip()
		print(line.replace('python', 'C'))


# Guest
# name = input("Enter your name: ")

# filename = 'text_files/guest.txt'

# with open(filename, 'w') as file_object:
# 	file_object.write(name)


# Guest Book

# prompt = "\nEnter your name: "
# prompt += "\n(or) Enter 'quit' to exit the program: "

# message = ' '

# while message != 'quit':

# 	message = input(prompt)

# 	if message != 'quit':
# 		greeting = f"\nHi {message}! Have a great day.\n"
# 		print(greeting)

# 	filename = 'text_files/guest_book.txt'

# 	with open(filename, 'a') as file_object:
# 		file_object.write(greeting)


# Programming Poll

prompt = "\nEnter your name: "
prompt += "\n(or) Enter 'quit' to exit the program...  \n"

message = ' '

while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(f"\nHi {message}! Nice to meet you and i have a question for you...")
		print("Why do like rogramming?\n")

		text = input()

		filename = 'text_files/programming_poll.txt'

		with open(filename, 'a') as file_object:
			file_object.write(f"Name: {message}\n")
			file_object.write(text+'\n')

