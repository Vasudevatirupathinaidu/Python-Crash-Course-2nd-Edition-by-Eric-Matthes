# Stroing data
# Using json.dump()

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'text_files/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)