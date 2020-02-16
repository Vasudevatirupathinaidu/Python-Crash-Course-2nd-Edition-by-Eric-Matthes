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