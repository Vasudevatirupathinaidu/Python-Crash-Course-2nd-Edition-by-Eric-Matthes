# Learning Python
# filename = 'text_files/learning_python.txt'

# with open(filename) as file_object:
# 	content = file_object.read()

# print(content)
# print("\n")


# with open(filename) as file_object:
# 	for line in file_object:
# 		print(line.strip())
# print("\n")


# with open(filename) as file_object:
# 	lines = file_object.readlines()

# print(lines)
# for line in lines:
# 	print(line.strip())
# print("\n")



# Learning C
# filename = 'text_files/learning_python.txt'

# with open(filename) as file_object:
# 	lines = file_object.readlines()

# for line in lines:
# 	if 'python' in line:
# 		line = line.strip()
# 		print(line.replace('python', 'C'))
# print("\n")



# Guest
# name = input("\nEnter your name: ")

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
# prompt = "\nEnter your name: "
# prompt += "\n(or) Enter 'quit' to exit the program...  \n"

# message = ' '

# while message != 'quit':
# 	message = input(prompt)
# 	if message != 'quit':
# 		print(f"\nHi {message}! Nice to meet you and i have a question for you...")
# 		print("Why do like rogramming?\n")

# 		text = input()

# 		filename = 'text_files/programming_poll.txt'

# 		with open(filename, 'a') as file_object:
# 			file_object.write(f"Name: {message}\n")
# 			file_object.write(text+'\n')



# Addition
# number1 = input("\nPlease enter the first number: ")
# number2 = input("\nPlease enter the second number: ")

# try:
# 	addition = int(number1) + int(number2)

# except ValueError:
# 	print("\nGiven input value is not a number. Kindly enter the number correctly.\n")
# else:
# 	print(f"\nThe sum of number1 and number2 is: {addition}\n")
# print("\n")


# Addition calculator
# while True:

# 	number1 = input("\nPlease enter the first number: ")
# 	if number1 == 'q':
# 		break

# 	number2 = input("\nPlease enter the second number: ")
# 	if number2 == 'q':
# 		break

# 	try:
# 		addition = int(number1) + int(number2)

# 	except ValueError:
# 		print("\nGiven input value is not a number. Kindly enter the number correctly.\n")
# 	else:
# 		print(f"\nThe sum of number1 and number2 is: {addition}\n")
# print("\n")



# Cats and Dogs
# def cats_dogs(filename):

# 	try:
# 		with open(filename, encoding='utf-8') as file_object:
# 			content = file_object.read()

# 	except FileNotFoundError:
# 		print(f"Sorry, Your file {filename} is not found.")

# 	else:
# 		if filename[-8:-4] == 'cats':
# 			print("Cat names: ")
# 		else: 
# 			print("Dog names: ")

# 		print(content)


# filenames = ['text_files/cats.txt', 'dogs.txt']

# for filename in filenames:
# 	cats_dogs(filename)
# 	print("\n")



# Silent Cats and Dogs
# def cats_dogs(filename):

# 	try:
# 		with open(filename, encoding='utf-8') as file_object:
# 			content = file_object.read()

# 	except FileNotFoundError:
# 		# print(f"Sorry, Your file {filename} is not found.")
# 		pass

# 	else:
# 		if filename[-8:-4] == 'cats':
# 			print("Cat names: ")
# 		else: 
# 			print("Dog names: ")

# 		print(content)


# filenames = ['text_files/cats.txt', 'dogs.txt']

# for filename in filenames:
# 	cats_dogs(filename)
# 	print("\n")



# Common words
def count_common_words(filename, commonword):

	try:
		with open(filename) as file_object:
			content = file_object.read()

		words_count = content.lower().count(commonword)

	except FileNotFoundError:
		print(f"Sorry, file {filename} is not found.")

	else:
		print(f"'{commonword}' appears in {filename} about {words_count} times.")		


filename = 'text_files/common_words.txt'

count_common_words(filename, 'the')
