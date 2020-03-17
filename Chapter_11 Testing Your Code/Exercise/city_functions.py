# City, Country

# def get_city_country_name(city_name, country_name):
#     return f"{city_name.title()}, {country_name.title()}"



# Population

def get_city_country_name(city_name, country_name, population=0):

    if population:
        return f"{city_name.title()}, {country_name.title()} - population {population}."
    else:
        return f"{city_name.title()}, {country_name.title()}"