# Import Multiple Classes from a Module

# from car_1 import Car, ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2020)
# print(my_beetle.get_descriptive_name())

# my_tesla = Car('tesla', 'roadster', 2020)
# print(my_tesla.get_descriptive_name())



# Importing an Entire Module
# import car_1

# my_beetle = car_1.Car('volkswagen', 'beetle', 2020)
# print(my_beetle.get_descriptive_name())

# my_tesla = car_1.Car('tesla', 'roadster', 2020)
# print(my_tesla.get_descriptive_name())


# Importing All Classes from a Module

# from module_name import * --> This method is not recommended.


# Importing a Module into a Module

from car_2 import Car
from electric_car_2 import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2020)
print(my_beetle.get_descriptive_name())

my_tesla = Car('tesla', 'roadster', 2020)
print(my_tesla.get_descriptive_name())