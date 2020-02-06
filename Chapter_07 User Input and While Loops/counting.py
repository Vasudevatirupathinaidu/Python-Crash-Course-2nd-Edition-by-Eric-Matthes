# The while loop in action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print("\n")


# Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


# Avoiding Infinite Loops
'''If your program gets stuck in an infinite loop, press ctrl-C'''