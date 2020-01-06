# Person

person = {
    'first_name' : 'Vasudeva',
    'last_name' : 'Bonu',
    'age' : 27,
    'city' : 'Bangalore',
}

print(f"Hola! My name is {person['last_name']} {person['first_name']}. I am {person['age']} years old guy lives in {person['city']}.")
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



# Rivers

rivers = {
    'krishna' : 'vijayawada',
    'yamuna' : 'agra',
    'kaveri' : 'tiruchirapalli',
}

for river, city in rivers.items():
    print(f"The {river} river runs through {city}.")
print("\n")

for river in rivers.keys():
    print(river)
print("\n")

for city in rivers.values():
    print(city)
print("\n")


# Polling

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

members = ['phil', 'daniel', 'edward', 'erin', 'sarah']

for member in members:
    if member in favorite_languages.keys():
        print(f"{member.title()}, thank you for taking the poll.")
    else:
        print(f"{member.title()}, please take our poll.")
print("\n")


# People

person_1 = {
    'first_name' : 'vasu',
    'last_name' : 'bonu',
    'age' : 27,
    'city' : 'bangalore',
}

person_2 = {
    'first_name' : 'deva',
    'last_name' : 'bonu',
    'age' : 26,
    'city' : 'gurgaon',
}

person_3 = {
    'first_name' : 'tiru',
    'last_name' : 'bonu',
    'age' : 25,
    'city' : 'bangalore',
}

people = [person_1, person_2, person_3]

for person in people:
    print(person)
print("\n")


# Pets

pet_1 = {
        'owner_s name': 'vasu',
        'pet_s name': 'DogA',
    }

pet_2 = {
        'owner_s name': 'deva',
        'pet_s name': 'DogB',
    }

pet_3 = {
        'owner_s name': 'tiru',
        'pet_s name': 'DogC',
    }

pet_4 = {
        'owner_s name': 'naidu',
        'pet_s name': 'DogD',
    }


pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"Pet Owner's name: {pet['owner_s name']}")
    print(f"Pet's name: {pet['pet_s name']}\n")


# Favorite places

favorite_places = {
    'deva':['goa', 'kochi', 'udupi'],
    'vasu':['kochi', 'araku', 'shillong'],
    'tiru':['udupi', 'ladakh', 'west godavari'],
}

for names, places in favorite_places.items():
    for place in places:
        print(f"{(names.title())}'s favorite place is {place.title()}.")
    print("\n")


# Favorite numbers

persons = {
    'ching' : [5, 2, 9],
    'chang' : [6, 1],
    'chung' : [1, 8, 7],
    'ding' : [9, 3, 6],
    'ping' : [1, 2],
    'dang' : [4, 0],
}

for names, numbers in persons.items():
    for number in numbers:
        print(f"{names.title()}'s favorite number is {number}.")
    print("\n")


# Cities

cities = {
    'vizag': {
        'country': 'india',
        'population': '21 lakhs',
        'favoriteSpot': 'beach',
    },
    'bangalore': {
        'country': 'india',
        'population': '84 lakhs',
        'favoriteSpot': 'bangalore palace',
    },
    'rajahmundry': {
        'country': 'india',
        'population': '4 lakhs',
        'favoriteSpot': 'godavari arch bridge',
    },
}

for name, data in cities.items():
    print(f"City name {name.title()}: ")
    for info, data_2 in data.items():
        print(f"{info.title()}: {data_2.title()}")
    print("\n")


# Extensions


favorite_languages = {
    'jen' : 'c++',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'javascript',
}

new_members = ['david', 'lucy', 'john']

for member in new_members:
    if member == 'lucy':
        favorite_languages[member] = 'go'
    elif member == 'john':
        favorite_languages[member] = 'java'
    elif member == 'david':
        favorite_languages[member] = 'python'

print(f"\nList of names: ")
for name in favorite_languages.keys():
    print(f"{name.title()}")

print(f"\nList of languages: ")
for language in favorite_languages.values():
    print(f"{language.title()}")
print("\n")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print("\n")