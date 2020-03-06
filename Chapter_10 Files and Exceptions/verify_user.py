# Verify User

import json

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

        correct_username = input(f"\nAre you {username}? (y/n) ")

        if correct_username == 'y':
            print(f"\nWelcome back, {username}!")

        else:

            username = get_new_username()
            print(f"\nWe'll remember you when you come back, {username}!")

    else:
        username = get_new_username()
        print(f"\nWe'll remember you when you come back, {username}!")

greet_user()