# Looping through an entire list
# for loop - computer automates repetitive tasks
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
print("\n")


# Doing more work within a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
print("\n")

# Avoiding indentation errors

# Forgetting to indent
magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)

# Forgetting to indent additional lines
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Indenting unnecessarily
message = 'Hello Python World!'
	# print(message)

# Indenting unnecessarily after the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

	# print("Thank you, everyone. That was a great magic show!")
	