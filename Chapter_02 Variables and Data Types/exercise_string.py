# f-string
last_name = "Bonu"
middle_name = "Deva"
message = "{} {}".format(last_name, middle_name)
print(message)
message = f"{last_name} {middle_name}"
print(message)

print("\n")


# Personal message
name = "Deva"
message = f"Hello {name}, would you like to learn Python today?"
print(message)

print("\n")


# Name cases
fullname = "vasudev tirupathi naidu"
print(fullname.title())
print(fullname.upper())
print(fullname.lower())

print("\n")


# Famous quote
quote = f'\t\t\t\tAlbert Einstein once said, "A person who never made a\n\t\t\t\tmistake never tried anything new."'
print(quote)

print("\n")


# Famous quote 2
famous_person = "Christopher Nolan"
message = f'\t\t\t\t{famous_person} once said, "You can tell a lot about people from their stuff."'
print(message)

print("\n")


# Stripping Names
person = "\tDeva\n";
print(person)
print(person.rstrip())
print(person.lstrip())
print(person.strip())
