# Favorite Number Remebered

import json

filename = 'text_files/favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)

except FileNotFoundError:

    favorite_number = input("\nWhat is your favorite number? ")

    with open(filename, 'w') as f:
        number = json.dump(favorite_number, f)
        print(f"\nThanks!, I will remember your favorite number i.e {favorite_number}.")
else:
    print(f"\nWelcome back! I still remember your favorite number i.e {favorite_number}")