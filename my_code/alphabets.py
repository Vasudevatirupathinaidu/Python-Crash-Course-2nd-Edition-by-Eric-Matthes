import string

print(dir(string))
print("\n")

print(list(string.ascii_lowercase))
print(list(string.ascii_uppercase))
print("\n")


# list comprehension
letters = [chr(letter) for letter in range(ord('a'), ord('z')+1)]

print(letters)
print("\n")


# map
print(list(map(chr, range(ord('a'), (ord('z')+1)))))
print("\n")


# exercise
quote1 = "It’s better to be a lion for a day than a sheep all your life."

list_quote1 = list(quote1)
while " " in list_quote1:
    list_quote1.remove(" ")

print(f"Most repeated letter in quote1: {max(set(list_quote1), key=list_quote1.count)}")

# quote2
with open("quote2.txt") as f:
    quote2 = f.read()

list_quote2 = list(quote2.lower())
# while " " in list_quote2:
#     list_quote2.remove(" ")

letter_number = [(quote2.count(letter),letter) for letter in set(list_quote2)]

letter_number1 = sorted(letter_number, reverse=True)

if letter_number1[0][1] == ' ' or letter_number1[0][1] == '.':
    del letter_number1[0]
if letter_number1[1][1] == ' ' or letter_number1[1][1] == '.':
    del letter_number1[1]

print(f"Most repeated letter in quote2: {letter_number1[0][1]}")
print("\n")


# Unpacking operator
numbers = [1, 2, 3]

print([*'abc', *numbers])
print(list('abc')+list(numbers))


message = 'Thanks to the flexibility of Python and the powerful ecosystem of packages, the Azure CLI supports features such as autocompletion (in shells that support it), persistent credentials, JMESPath result parsing, lazy initialization, network-less unit tests, and more.'

print(list(filter(lambda x: x.isalpha(),[*message])))

# print(dir(str))