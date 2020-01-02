# Conditional tests
# String
car = 'audi'
print("Is car == 'audi'? I predict True.")
print(car == 'audi')

print("Is car == 'subaru'? I predict False.")
print(car == 'subaru')

car = 'Audi'
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car.lower() == 'audi'? I predict True.")
print(car.lower() == 'audi')

car = 'subaru'
print("Is car != 'audi'? I predict True.")
print(car != 'audi')

print("Is car != 'subaru'? I predict False.")
print(car != 'subaru')
print("\n")


# Number
number = 21
print(number == 21)
print(number != 21)
print(number >= 22)
print(number <= 23)
print(number > 18)
print(number < 21)
print("\n")

age_0 = 18
age_1 = 21
print(age_0 >= 18 and age_1 <= 22)
print(age_0 > 19 and age_1 <= 21)
print(age_0 >= 18 or age_1 <= 22)
print(age_0 > 19 or age_1 <= 22)
print("\n")


# List
numbers = [1, 4, 6, 9, 3, 2]
print(8 in numbers)
print(3 in numbers)
print(7 not in numbers)
print(6 not in numbers)