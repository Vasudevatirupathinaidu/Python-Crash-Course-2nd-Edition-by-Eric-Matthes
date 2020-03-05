# Exceptions
'''Python uses special objects called exceptions to manage errors that arise during a program's execution. Exceptions are handled with try-except blocks'''

# Handling the ZeroDivisionError Exception
# Using try-except blocks

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")



