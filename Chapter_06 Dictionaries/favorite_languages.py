# A dictionary of similar objects

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")


# Looping

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print("\n")


# list comprehension

[print(f"{name.title()}'s favorite language is {language.title()}.") for name, language in favorite_languages.items()]
print("\n")


# Looping through all the keys in a dictionary

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

for name in favorite_languages.keys():
    print(name.title())
print("\n")


# Looping through the keys is actually the default behavior when looping through a dictionary, so you can omit the key() method here.
for name in favorite_languages:
    print(name.title())
print("\n")


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
print("\n")


# Use the key() method to find out if a particular person was polled.

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!\n")


# Looping through a dictionary's keys in a particular order
# Using sorted() function

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print("\n")


# Looping through all values in a dictionary

print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
print("\n")


# To see each language chosen without repetition, we can use a set. A set is a collection in which each item must be unique.

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())
print("\n")


# You can build a set directly using braces and separating the elements with commas. Unlike lists and dictionaries, sets do not retain items in any specific order.

languages = {'python', 'ruby', 'python', 'c'}
print(languages)
print("\n")


# A List inside a dictionary

favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language.title()}")
print("\n")