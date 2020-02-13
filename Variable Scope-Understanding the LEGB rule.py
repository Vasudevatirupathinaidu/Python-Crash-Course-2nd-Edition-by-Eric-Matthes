'''
LEGB
Local, Enclosing, Global, Bulit-in
'''

import builtins
print(dir(builtins))
print("\n")


x = 'global x'

def test(z):
    global x  # bad practice
    x = 'local x'
    # print(y)
    print(x)
    print(z)


test('local z')
print(x)
print("\n")


# Built-in

# def min():
#     pass
# m = min([5, 3, 1, 7, 2, 4])
# print(m) # Causes error because Python found min function in the global scope before it fell back to the buil-in scope. So, we have to change min() function name to some other like my_min() in order to run this code


# Enclosing

def outer():
    x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print("\n")


# nonlocal statement

def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x' # x got overwritten here
        print(x)

    inner()
    print(x)

outer()
print("\n")


# Scope chain

x = 'global x'

def outer():
    # x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)
print("\n")