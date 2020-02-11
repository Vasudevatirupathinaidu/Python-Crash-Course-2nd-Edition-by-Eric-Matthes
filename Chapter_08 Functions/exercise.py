# Message
def display_message():
    print("Hello Everyone! In this chapter we are going to learn about a function.")
display_message()
print("\n")


# Favorite Book
def favorite_book(title, author):
    print(f"My favorite book is {title.title()} by {author.title()}.")
favorite_book('thinking in numbers', 'daniel tammet')
print("\n")


# T-Shirt
def make_shirt(size, message):
    print(f"\nI am going to make a {size} t-shirt.")
    print(f"\nIt will say, {message}.")
make_shirt('large', 'I Love Python')
make_shirt(message="I prefer medium size t-shirt", size='medium')
print("\n")

# Large Shirts
def make_shirt(size='large', message="I Love Python"):
    print(f"\nI am going to make a {size} t-shirt.")
    print(f"It will say, '{message}'.")
make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Long time no see')
print("\n")

# Cities
def describe_city(city, country = 'India'):
    print(f"\n{city} is in {country}.")

describe_city('Vizag')
describe_city(city = 'Bangalore')
describe_city(city = 'California', country = 'USA')

