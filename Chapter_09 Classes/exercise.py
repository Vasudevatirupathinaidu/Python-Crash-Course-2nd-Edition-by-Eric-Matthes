# Restaurant
class Restaurant:
    def __init__(self, restarant_name, cuisine_type):
        self.restarant_name = restarant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The {self.restarant_name}\'s {self.cuisine_type} is so good.')

    def open_restaurant(self):
        print(f"The {self.restarant_name} is open.")

restarant = Restaurant('King', 'Pizza')
print(restarant.restarant_name)
print(restarant.cuisine_type)
restarant.describe_restaurant()
restarant.open_restaurant()
print("\n")


# Three Restaurants
restarant1 = Restaurant('Queen', 'Burger')
restarant1.describe_restaurant()

restarant2 = Restaurant('My Restaurant', 'Seafood')
restarant2.describe_restaurant()

restarant3 = Restaurant('Gentleman', 'Aloofry')
restarant3.describe_restaurant()
print("\n")


# Users
class Users:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = first_name + last_name + '@gmail.com'

    def describe_user(self):
        print('User\'s Information: ')
        fullname = f'{self.first_name} {self.last_name}'
        print(f'Fullname: {fullname}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')

    def greet_user(self):
        print(f'Hello {self.first_name}! Welcome to the world of python.')

user1 = Users('vasudeva', 'tirupathinaidu', 27)
user1.describe_user()
user1.greet_user()
print("\n")

user2 = Users('john', 'wick', 28)
user2.describe_user()
user2.greet_user()
print("\n")

user3 = Users('christopher', 'nolan', 29)
user3.describe_user()
user3.greet_user()
print("\n")


# Number Served
class Restaurant:
    def __init__(self, restarant_name, cuisine_type):
        self.restarant_name = restarant_name
        self.cuisine_type = cuisine_type
        self.number_served = 15

    def describe_restaurant(self):
        print(f'The {self.restarant_name}\'s {self.cuisine_type} is so good.')

    def open_restaurant(self):
        print(f"The {self.restarant_name} is open.")

    def set_number_served(self):
        print(f'The number served by the {self.restarant_name}: {self.number_served}')

    def increment_number_served(self, added_memebers):
        self.number_served += added_memebers


restaurant = Restaurant('King', 'Pizza')
print(f'The number served by the {restaurant.restarant_name}: {restaurant.number_served}')

restaurant_1 = Restaurant('Olamisso', 'Noodles')
restaurant_1.set_number_served()

restaurant_2 = Restaurant('Queen', 'Burger')
restaurant_2.increment_number_served(200)
restaurant_2.set_number_served()

restaurant_2.increment_number_served(2000)
restaurant_2.set_number_served()

restaurant_2.increment_number_served(400)
restaurant_2.set_number_served()
print("\n")


# Login Attempts
class Users:
    def __init__(self, first_name, last_name, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = first_name + last_name + '@gmail.com'
        self.login_attempts = login_attempts

    def describe_user(self):
        print('User\'s Information: ')
        fullname = f'{self.first_name} {self.last_name}'
        print(f'Fullname: {fullname}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')

    def greet_user(self):
        print(f'Hello {self.first_name}! Welcome to the world of python.')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'Login Attempts: {self.login_attempts}')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Reset to {self.login_attempts}.')

user = Users('vasu', 'deva', 27, 0)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.reset_login_attempts()
print("\n")


# Ice Cream Stand
class Restaurant:
    def __init__(self, restarant_name, cuisine_type):
        self.restarant_name = restarant_name
        self.cuisine_type = cuisine_type
        self.number_served = 15

    def describe_restaurant(self):
        print(f'The {self.restarant_name}\'s {self.cuisine_type} is so good.')

    def open_restaurant(self):
        print(f"The {self.restarant_name} is open.")

    def set_number_served(self):
        print(f'The number served by the {self.restarant_name}: {self.number_served}')

    def increment_number_served(self, added_memebers):
        self.number_served += added_memebers


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type = 'Icecream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def iceflover(self):
        print("\nWe have the following flavors: ")
        for flavor in icecream.flavors:
            print(f" - {flavor.title()}")


icecream = IceCreamStand('King')
icecream.flavors = ['vanilla', 'chocolate', 'black current']

icecream.iceflover()
print("\n")


# Admin
class Users:
    def __init__(self, first_name, last_name, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = first_name + last_name + '@gmail.com'
        self.login_attempts = login_attempts

    def describe_user(self):
        print('User\'s Information: ')
        fullname = f'{self.first_name} {self.last_name}'
        print(f'Fullname: {fullname}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')

    def greet_user(self):
        print(f'Hello {self.first_name}! Welcome to the world of python.')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'Login Attempts: {self.login_attempts}')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Reset to {self.login_attempts}.')


class Admin(Users):
    def __init__(self, first_name, last_name, age, login_attempts):
        super().__init__(first_name, last_name, age, login_attempts)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nThe Administrator's set of privileges: ")
        for privilege in self.privileges:
            print(f" - {privilege}")

john = Admin('john', 'wick', 28, 3)

print(f"{john.first_name.title()} {john.last_name.title()}")
print(f"{2*' '}Username: {john.first_name.title()} {john.last_name.title()}")
print(f"{2*' '}Email: {john.first_name}{john.last_name}@gmail.com")
print(f"{2*' '}Age: {john.age}")

john.show_privileges()
print("\n")


# Privileges
class Users:
    def __init__(self, first_name, last_name, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = first_name + last_name + '@gmail.com'
        self.login_attempts = login_attempts

    def describe_user(self):
        print('User\'s Information: ')
        fullname = f'{self.first_name} {self.last_name}'
        print(f'Fullname: {fullname}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')

    def greet_user(self):
        print(f'Hello {self.first_name}! Welcome to the world of python.')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'Login Attempts: {self.login_attempts}')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Reset to {self.login_attempts}.')


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print("\nThe Administrator's set of privileges: ")
        for privilege in self.privileges:
            print(f" - {privilege}")


class Admin(Users):
    def __init__(self, first_name, last_name, age, login_attempts):
        super().__init__(first_name, last_name, age, login_attempts)
        self.privi = Privileges()


john = Admin('john', 'wick', 28, 3)

print(f"{john.first_name.title()} {john.last_name.title()}")
print(f"{2*' '}Username: {john.first_name.title()} {john.last_name.title()}")
print(f"{2*' '}Email: {john.first_name}{john.last_name}@gmail.com")
print(f"{2*' '}Age: {john.age}")

john.privi.show_privileges()
print("\n")


# Battery Upgrade
