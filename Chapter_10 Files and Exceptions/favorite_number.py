# Favorite Number

import json

your_name = input("\nWhat is your name? ")
favorite_number = input("\nWhat is your favorite number? ")

filename = 'text_files/favorite_number.json'

with open(filename, 'w') as f:
    content = json.dump((your_name,favorite_number), f)
    print(f"\nThanks {your_name}, I will remember your favorite number i.e {favorite_number}.")
