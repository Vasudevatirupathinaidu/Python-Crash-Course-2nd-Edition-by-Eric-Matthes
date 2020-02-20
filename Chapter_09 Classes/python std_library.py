# Python Standard Library 
# random

# randint()
from random import randint

print(randint(1, 20))


# choice()
from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)