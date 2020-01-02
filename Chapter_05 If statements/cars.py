# if else statements
cars = ['audi', 'bmw', 'subaru', 'toyota']
print(cars)
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("\n")


# Conditional tests

# Checking for equality
car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

# Ignoring case when checking for equality# Testing 
# Testing for equality is case sensitive in python
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')
print(car)
