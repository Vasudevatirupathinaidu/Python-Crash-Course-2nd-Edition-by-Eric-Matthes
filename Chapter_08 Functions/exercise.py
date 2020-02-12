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
print("\n")


# City Names
def city_country(city, country):
    print(f'\n"{city}, {country}"')

city_country(city='Rajahmundry', country='India')
city_country('Vizag', 'India')
city_country(city='California', country='India')
print("\n")


# Album
def make_album(artist_name, album_title, no_of_songs=None):
    artist = dict()

    if no_of_songs:
        artist['Songs'] = no_of_songs

    artist['Artist'] = artist_name
    artist['Album'] = album_title

    return f"\n{artist}"

# Take inputs from users
name = input(f"\nPlease enter artist name: ")
album = input(f"\nPlease enter album title: ")
songcount = input("\nNumber of songs are in this album: ")

fav_album = make_album(name, album, songcount)
print(fav_album)


# User Albums
def make_album(artist_name, album_title, no_of_songs=None):
    artist = dict()

    artist['Artist'] = artist_name
    artist['Album'] = album_title

    if no_of_songs:
        artist['Songs'] = no_of_songs

    return f"\n{artist}"

# Take inputs from users
while True:
    print("\nPlease enter below details: ")
    print("Type 'q' to quit this task.")

    name = input("\nPlease enter artist name: ")
    if name == 'q':
        break

    album = input("\nPlease enter album title: ")
    if album == 'q':
        break

    songcount = input("\nNumber of songs are in this album: ")
    if songcount == 'q':
        break

    fav_album = make_album(name, album, songcount)

    print(fav_album)