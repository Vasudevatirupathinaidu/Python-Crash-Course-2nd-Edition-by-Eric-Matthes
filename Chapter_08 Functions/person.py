# Returning a Dictionary
def bulid_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person."""
    person = {'first':first_name, 'last':last_name}

    if age:
        person['age'] = age
    
    return person

musician = bulid_person('Vasudev', 'Bonu', age = 27)
print(musician)