# Return Values - The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function.


# Returning a Simple Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{last_name} {first_name}"
    return full_name.title()

musician = get_formatted_name('vasudeva', 'bonu')
print(musician)
print("\n")


def get_formatted_name(first_name, last_name, middle_name):
    """Return a full name, neatly formatted."""
    full_name = f"{last_name} {first_name} {middle_name}"
    return full_name.title()

musician = get_formatted_name('vasudeva', 'bonu', 'tirupathi naidu')
print(musician)
print("\n")


# Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{last_name} {first_name} {middle_name}"
    else:
        full_name = f"{last_name} {first_name}"

    return full_name.title()

musician = get_formatted_name('vasudeva', 'bonu')
print(musician)
musician = get_formatted_name('vasudeva', 'bonu', 'tirupathi naidu')
print(musician)