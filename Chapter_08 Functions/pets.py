# Passing Arguments

# Positional Arguments - When you call a function, Python must match each argument in the function call with a parameter in the function definition.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
print("\n")


# Order Matters in Positional Arguments

# Keyword Arguments - A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')
print("\n")


# Default Values
def describe_pet(pet_name, animal_type='hamster'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')
print("\n")


# Equivalent Function Calls
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
print("\n")

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')


# Avoiding Argument Errors
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet() - # TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
# print("\n")