# Stroing data
# Using json.load()

import json

filename = 'text_files/numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)