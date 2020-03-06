# Saving and Reading user-generated data

import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = 'text_files/username.json'

try:
    with open(filename) as f:
        username = json.load(f)

except FileNotFoundError:
    username = input("\nWhat is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!") 

print("\n")



# Refactoring

def get_stored_username():
    '''Get stored username if available.'''
    filename = 'text_files/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''Prompt for a new username.'''
    username = input("\nWhat is your name? ")
    filename = 'text_files/username.json'
    with open(filename, 'w') as f:
            json.dump(username, f)
    return username
    
def greet_user():
    '''Greet the user by name'''
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")

greet_user()