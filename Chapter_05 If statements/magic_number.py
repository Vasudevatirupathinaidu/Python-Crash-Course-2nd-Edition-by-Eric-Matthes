# Numerical comparisons
age = 18
print(age == 18)
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)
print("\n")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
print("\n")


# Checking multiple conditions
# keywords and & or

# Using 'and' keyword
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
print("\n")

# Using 'or' keyword
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_1 = 22
print(age_0 >= 21 or age_1 >= 21)
print("\n")


# Checking whether a value is in a list
# Using 'in' keyword
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
print("\n")

# Using 'not' keyword
print('mushrooms' not in requested_toppings)
print('pepperoni' not in requested_toppings)
print("\n")


