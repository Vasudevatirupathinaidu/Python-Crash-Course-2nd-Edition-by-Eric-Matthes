# The if-elif-else chain
age = 12

if age < 4:
    print("Your admission cost is $0.\n")
elif age < 18:
    print("Your admission cost is $25.\n")
else:
    print("Your admission cost is $40.\n")

# Much more concise way
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.\n")


# Using multiple elif blocks
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.\n")


# Omitting the else block
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age > 65:
    price = 20

print(f"Your admission cost is ${price}.\n")