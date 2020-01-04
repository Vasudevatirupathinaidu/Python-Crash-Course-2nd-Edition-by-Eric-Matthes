# A list in a dictionary
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

print(f"\n{pizza}")
print(f"\n{pizza['crust']}")
print(f"\n{pizza['toppings']}\n")

print(f"You ordered a {pizza['crust']} - crust pizza" 
    "with the following toppings: ")
for topping in pizza['toppings']:
    print(topping)
print("\n")


# display only values
for value in pizza.values():
    if type(value) is list:
        for topping in pizza['toppings']:
            print(topping)
    else:
        print(value)
print("\n")