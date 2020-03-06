# Exceptions
'''Python uses special objects called exceptions to manage errors that arise during a program's execution. Exceptions are handled with try-except blocks'''

# Handling the ZeroDivisionError Exception
# Using try-except blocks

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print("\n")


# Using exceptions to prevent crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
