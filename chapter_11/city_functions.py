def city_country(city, country, population=''):
    if population:
        country_population = f"{city.title()}, {country.title()} - population {population}"
    else:
        country_population = f"{city.title()}, {country.title()}"
    return country_population