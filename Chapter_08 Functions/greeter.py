# Defining a Function
def greet_user():
    """Display a simple greeting.""" # docstring - Which describes what the function does.
    print("Hello Python Lovers!")

greet_user()


# Passing information to a function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('deva')
greet_user('vasu')

# Note: username is a parameter and 'deva', 'vasu' are referred as arguments