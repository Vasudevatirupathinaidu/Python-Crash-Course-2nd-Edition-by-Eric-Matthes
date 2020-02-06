# Rental Car
# users_car_name = input("What kind of rental car you would like to ride? ")
# print(f"\nLet me see if i can find you a {users_car_name.title()}.")


# Restaurant Seating
# number_of_people = input("How many people are in your dinner group? ")
# number_of_people = int(number_of_people)

# if number_of_people > 8:
#     print("\nPlease wait for sometime for a dinner table.")
# else:
#     print("\nYour table is ready. Please join us.")


# Multiples of Ten
# number = input("Please a enter a number: ")
# number = int(number)
# if number % 10 == 0:
#     print(f"{number} is a multiple of 10.")
# else:
#     print(f"{number} is not a multiple of 10.")


# Pizza Toppings
# prompt = "\nPlease enter your favorite topping:"
# prompt += "\nEnter 'quit' to end the program. "

# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"\nI'll add {topping} to your pizza.")
#     else:
#         break


# Movie Tickets
# enter_age = "\nWhat is your age?"
# enter_age += "\nEnter 'quit' when you are finished. "

# while True:
#     age = input(enter_age)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age < 3:
#         print("\nThe movie ticket is free.")
#     elif age > 3 and age < 12:
#         print("\nThe movie ticket cost is $10.")
#     elif age > 12:
#         print("\nThe movie ticket cost is $15.")


# Three Exits
# Pizza Toppings
# prompt = "\nPlease enter your favorite topping:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         print(f"\nI'll add {topping} to your pizza.")


# Infinity
# i = 0
# while i < 10:
#     print(i)


# Deli
# sandwich_orders = ['paneer', 'mushroom', 'chicken', 'tuna']
# finished_sanwiches = []

# while sandwich_orders:
#     finished_sanwich = sandwich_orders.pop()
#     print(f"I'm working on your {finished_sanwich} sandwich.")
#     finished_sanwiches.append(finished_sanwich)
# print("\n")
# for finished_sanwich in finished_sanwiches:
#     print(f"I made your {finished_sanwich} sandwich.")


# No Pastrami
# sandwich_orders = ['pastrami', 'paneer', 'mushroom', 'chicken', 'pastrami', 'tuna', 'pastrami']
# finished_sanwiches = []

# print("\nSorry, The deli has run out of pastrami.\n")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     finished_sanwich = sandwich_orders.pop()
#     print(f"I'm working on your {finished_sanwich} sandwich.")
#     finished_sanwiches.append(finished_sanwich)
# print("\n")
# for finished_sanwich in finished_sanwiches:
#     print(f"I made your {finished_sanwich} sandwich.")


# Dream Vacation
prompt = "\nIf you could visit one place in the world, where would you go?"
prompt += "\nEnter 'quit' to end the program. "
persons = {}

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)