# Person

person = {
    'first_name' : 'Vasudeva',
    'last_name' : 'Bonu',
    'age' : 27,
    'city' : 'Bangalore',
}

print(f"Hola! My name is {person['last_name']} {person['first_name']}. I am {person['age']} years old, lives in {person['city']}.")
print("\n")


# Favorite numbers

persons = {
    'ching' : 5,
    'chang' : 6,
    'chung' : 1,
    'ding' : 9,
    'ping' : 1,
    'dang' : 4,
}

# Method 1

print(f"Hi! My name is ching. My favorite number is {persons['ching']}.")
print(f"Hi! My name is chang. My favorite number is {persons['chang']}.")
print(f"Hi! My name is chung. My favorite number is {persons['chung']}.")
print(f"Hi! My name is ding. My favorite number is {persons['ding']}.")
print(f"Hi! My name is ping. My favorite number is {persons['ping']}.")
print(f"Hi! My name is dang. My favorite number is {persons['dang']}.")
print("\n")


# Method 2 - for loop

for key, value in persons.items():
    print(f"Hi! My name is {key.title()}. My favorite number is {value}.")
print("\n")

# Method 3 - list comprehension

[print(f"Hi! My name is {key.title()}. My favorite number is {value}.") for key, value in persons.items()]

print('\n')

print('\n'.join([(f"Hi! My name is {key.title()}. My favorite number is {value}.") for key, value in persons.items()]))

print("\n")


# Glossary

glossary = {
    'string' : 'A series of characters.',
    'list' : 'A collection of items.',
    'method' : 'A method is an action that python can perform on a piece of data.',
    'if-elif-else' : 'if-elif-else statement chains are used for decision making.',
    'for_loop' : 'For loops are used for sequential traversal.',
    'dictionary' : 'A collection of key-value pairs.',
    'get method' : 'It can add a default value to key.',
    'set' : 'It can remove duplicate values.',
    'in and not' : 'in and not are special keywords, mainly used for decision making.',
}

# Method 1

print(f"String: {glossary['string']}")
print(f"List: {glossary['list']}")
print(f"Method: {glossary['method']}")
print(f"if-elif-else: {glossary['if-elif-else']}")
print(f"for_loop: {glossary['for_loop']}")
print(f"dictionary: {glossary['dictionary']}")
print(f"get method: {glossary['get method']}")
print(f"set: {glossary['set']}")
print(f"in and not: {glossary['in and not']}")


# Method 2 - for loop

for key, value in glossary.items():
    print(f"{key.title()}: {value}")
print("\n")


# Method 3 - list comprehension

[print(f"{key.title()}: {value}") for key, value in glossary.items()]
print("\n")

print('\n'.join([(f"{key.title()}: {value}") for key, value in glossary.items()]))
print("\n")

