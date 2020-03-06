# Saving and Reading user-generated data

import json

filename = 'text_files/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")