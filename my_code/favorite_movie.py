# Storing and Retrieving

import json

def get_stored_info():
    try:
        filename = 'test.json'

        with open(filename) as f:
            content = json.load(f)

    except FileNotFoundError:
        return None
    else:
        return content

def get_new_info():

    your_name = input("\nWhat is your name? ")
    favorite_movie = input("\nWhat is your favorite movie? ")

    info = dict(name=your_name, favorite=favorite_movie)

    filename = 'test.json'

    with open(filename, 'w') as f:
        json.dump(info, f)

    return your_name
       
def greet_user():

    content = get_stored_info()

    if content:
        correct = input(f"\nAre you {content['name']}?(y/n) ")
        if correct == 'y':
            print(f"\nWelcome back {content['name']}!. I still remember your favorite movie {content['favorite']}.")
        else:
            your_name = get_new_info()
            print(f"\nThanks {your_name}!, I will remember your favorite movie.")
    else:
        your_name = get_new_info()
        print(f"\nThanks {your_name}!, I will remember your favorite movie.")

greet_user()