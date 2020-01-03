# Dictionaries - It is a collection of key-value pairs.

# A simple dictionary
alien_0 = {
'color' : 'green',
'points' : 5
}

print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
print("\n")


# Accessing values in a dictionary
alien_0 = {
'color' : 'green',
'points' : 5
}

new_points = alien_0['points']
print(f"You just earned {new_points} points!\n")


# Adding new key-value pairs
alien_0 = {
'color' : 'green',
'points' : 5
}

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("\n")


# Starting with an empty dictionary
alien_0 = {}

print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
print("\n")


# Modifying values in a dictionary
alien_0 = {
    'color' : 'green'
}

print(f"THe alien is {alien_0['color']}")

alien_0 = {
    'color' : 'yellow'
}

print(f"The alien is now {alien_0['color']}\n")


# One more interesting example
alien_0 = {
    'x_position': 0,
    'y_position': 0,
    'speed' : 'medium'
}

print(f"Original position: {alien_0['x_position']}.\n")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}.\n")


# Removing key-value pairs
alien_0 = {
    'color' : 'green',
    'points' : 5
}

print(alien_0)

del alien_0['points']
print(alien_0)
print("\n")