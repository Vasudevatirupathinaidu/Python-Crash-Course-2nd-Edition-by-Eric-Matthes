# Guessing number game
import random
guessing_number = random.randint(1,100)

while True:

    number = input('Guess a number b/w 1 to 100: ')
    my_number = int(number)

    if (my_number == guessing_number):
        print(f"You won! Your number {my_number} is the guessing number")
        break

    elif (my_number > guessing_number):
        print(f"Your number {my_number} is higher than guessing number")

    elif (my_number < guessing_number):
        print(f"Your number {my_number} is lower than guessing number")
    