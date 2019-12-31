# Names
print("\n\n\n")
print("Names")
names = ['vasu', 'deva', 'tirupathi', 'naidu']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])


# Greetings
print("\n\n\n")
print("Greetings")
print(f"Hello, {names[0]}! Good to see you again.")
print(f"Hello, {names[1]}! Good to see you again.")
print(f"Hello, {names[2]}! Good to see you again.")
print(f"Hello, {names[3]}! Good to see you again.")


# Your Own list
print("\n\n\n")
print("Your Own List")
my_list = ['Prestige', 'Inception', 'The Dark Knight']
print(f"{my_list[0]}: Are you watching closely?")
print(f"{my_list[1]}: You mustn't be afraid to dream a little bigger darling")
print(f"{my_list[2]}: Why So Serious?")


# Guest List
print("\n\n\n")
print("Guest List")
persons = [' albert einstein', 'srinivasa ramanujan', 'leonardo da vinci']
print(f"Hi {persons[0].title()}! I would like to invite you for a dinner.")
print(f"Hi {persons[1].title()}! I would like to invite you for a dinner.")
print(f"Hi {persons[2].title()}! I would like to invite you for a dinner.")


# Changing Guest List
print("\n\n\n")
print("Changing Guest List")
I_am_not = persons[0].title()
print(f"{I_am_not} said, He couldn't make the dinner this time.")
print(persons)
persons[0] = 'richard feynman'
print(persons)
print(f"Hi {persons[0].title()}! I would like to invite you for a dinner.")
print(f"Hi {persons[1].title()}! I would like to invite you for a dinner.")
print(f"Hi {persons[2].title()}! I would like to invite you for a dinner.")


# More Guests
print("\n\n\n")
print("More Guests")
persons = ['albert einstein', 'srinivasa ramanujan', 'leonardo da vinci']
persons.insert(0, 'richard feynman')
persons.insert(2, 'newton')
persons.append('antonio vivaldi')
print(persons)
print(f"Hi {persons[0].title()}! I would like to invite you for a dinner.")
print(f"Hi {persons[1].title()}! I would like to invite you for a dinner.")
print(f"Hi {persons[2].title()}! I would like to invite you for a dinner.")
print(f"Hi {persons[3].title()}! I would like to invite you for a dinner.")
print(f"Hi {persons[4].title()}! I would like to invite you for a dinner.")
print(f"Hi {persons[5].title()}! I would like to invite you for a dinner.")
print("I found a bigger dinner table for us.")


# Shrinking Guest List
print("\n\n\n")
print("Shrinking Guest List")
print(persons)
print("Ouch! I have space for only two guests.")
print(f"Hello {persons.pop()}! I am really sorry to say that as i can't invite you for a dinner. I will make that work for the next time. Sorry once again for the inconvenience caused.")
print(f"Hello {persons.pop()}! I am really sorry to say that as i can't invite you for a dinner. I will make that work for the next time. Sorry once again for the inconvenience caused.")
print(f"Hello {persons.pop()}! I am really sorry to say that as i can't invite you for a dinner. I will make that work for the next time. Sorry once again for the inconvenience caused.")
print(f"Hello {persons.pop()}! I am really sorry to say that as i can't invite you for a dinner. I will make that work for the next time. Sorry once again for the inconvenience caused.")
print(f"Hi {persons[0].title()}! I would like to invite you for a dinner.")
print(f"Hi {persons[1].title()}! I would like to invite you for a dinner.")
print("Wow! we made it.")
del persons[0]
del persons[0]
print(persons)
print("Dinner has been successful. No more guests are in my list")


# Seeing the World
print("\n\n\n")
print("Seeing the World")
locations = ['italy', 'bali', 'paris', 'amsterdam', 'london']
print(locations)

# alphabetical order - temporary
print(sorted(locations))
print(locations)
print(sorted(locations, reverse = True))
print(locations)

# reverse - permanent
locations.reverse()
print(locations)
locations.reverse()
print(locations)

# sort - permanent
locations.sort()
print(locations)
locations.sort(reverse = True)
print(locations)


# Dinner Guests
print("\n\n\n")
print("Dinner Guests")
persons = ['albert einstein', 'srinivasa ramanujan', 'leonardo da vinci']
print(len(persons))


# Every Function
print("\n\n\n")
print("Every Function")
group = []
group.append('hola')
group.append('cat')
group.insert(1, 'vizag')
group.append('drawing')
group.append('pen spinning')
print(group)
last_item = group.pop()
print(last_item)
print(group)
group.append('meditation')
print(group)
del group[0]
print(group)
group.insert(0, 'hello')
print(group)

# sort method - permanent
group.sort()
print(group)
group.sort(reverse = True)
print(group)

# sorted function- permanent
group = ['hello', 'vizag', 'cat', 'drawing', 'meditation']
print(sorted(group))
print(group)
print(sorted(group, reverse = True))
print(group)

# reverse method- permanent
group.reverse()
print(group)
group.reverse()
print(group)


# Intentional error
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])
motorcycles = []
print(motorcycles[-1])