# Using variables in strings

first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}" # f-string - f is for formate (Introduced in Python 3.6)

print(full_name)

print(f"Hello, {full_name.title()}!")

message = f"Hola, {full_name.title()}!"

print(message)


# format method introduced in Python 3.5

full_name = "{} {}".format(first_name, last_name)
print(full_name)