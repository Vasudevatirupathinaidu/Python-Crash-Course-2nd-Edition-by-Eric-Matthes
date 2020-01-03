# Using get() to access values
alien_0 = {
    'color' : 'green',
    'speed' : 'slow',
}

# print(alien_0['points'])

# You can use get() method to set a default value that will be returned if the required key doesn't exist.

point_value = alien_0.get('points', 'No pint value assigned.')
print(point_value)
