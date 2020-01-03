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
print("\n")


# Alien colors #1
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points.\n")

alien_color = 'yellow'
if alien_color == 'green':
    print("The player just earned 5 points.")

# Alien colors #2
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points.\n")
else:
    print("The player just earned 10 points.\n")

alien_color = 'red'
if alien_color == 'green':
    print("The player just earned 5 points.\n")
else:
    print("The player just earned 10 points.\n")


# Alien colors #3

alien_color = 'red'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
else:
    print("")

print(f"The player just earned {points} points.\n")


# Stages of life
age = 4

if age < 2:
    person = 'baby'
elif age >= 2 and age < 4:
    person = 'toddler'
elif age >= 4 and age < 13:
    person = 'kid'
elif age >= 13 and age < 20:
    person = 'teenager'
elif age >= 20 and age < 65:
    person = 'adult'
    print(f"The person is an {person}")
else:
    person = 'elder'
    print(f"The person is an {person}")

print(f"The person is a {person}\n")


# Favorite fruit

favorite_fruits = ['guava', 'apple', 'banana']

if 'guava' in favorite_fruits:
    print("My favorite fruit is guava.")
if 'apple' in favorite_fruits:
    print("My favorite fruit is apple.")
if 'banana' in favorite_fruits:
    print("My favorite fruit is banana.")
if 'jackfruit' in favorite_fruits:
    print("My favorite fruit is jackfruit.")
if 'orange' in favorite_fruits:
    print("My favorite fruit is orange.")

print("\n")


# Hello Admin
usernames = ['ching', 'chang', 'admin', 'chung', 'ding']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

print("\n")


# No users

usernames = []

if usernames:
    for username in usernames:
        print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

print("\n")


# Checking usernames

current_users = ['ching', 'chang', 'chung', 'ding', 'bing']
new_users = ['ADMIN', 'MAGNUS', 'CHING', 'CARLSEN', 'DING']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Username {new_user.lower()} is available.\n")
    if new_user.lower() not in current_users:
        print(f"{new_user.lower()}, You will need to enter a new username.\n")


# Original numbers
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    elif number == 4:
        print("4th")
    elif number == 5:
        print("5th")
    elif number == 6:
        print("6th")
    elif number == 7:
        print("7th")
    elif number == 8:
        print("8th")
    elif number == 9:
        print("9th")
    else:
        print("Out of range!")
