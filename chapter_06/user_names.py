#dictionary inside dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f'\nusername: {username}')
    fullname = f"{user_info['first']} {user_info['last']}"
    print(f"\tFullname: {fullname}")
    print(f"\tLocation: {user_info['location']}")
print()
#try it yourself
#6-7 people
people = []

person = {
    'first': 'mathew',
    'last': 'eric',
    'age': 43,
    'city': 'sydney'
}

people.append(person)

person = {
    'first': 'satish',
    'last': 'reddy',
    'age': 37,
    'city': 'silicon valley'
}
people.append(person)

person = {
    'first': 'naveen',
    'last': 'polishetty',
    'age': 35,
    'city': 'mumbai'
}
people.append(person)

for person in people:
    fullname = f"{person['first']} {person['last']}"
    print(f"{fullname}, lives in {person['city']} he is {person['age']} years old.")

#6-8 pets
pets = []
pet = {
    'name': 'rocky',
    'animal type': 'dog',
    'owner': 'eric',
}
pets.append(pet)

pet = {
    'name': 'brook',
    'animal type': 'cat',
    'owner': 'sunny',
}
pets.append(pet)
pet = {
    'name': 'blackie',
    'animal type': 'dog',
    'owner': 'prem',
}
pets.append(pet)

for pet in pets:
    print(f"\ni know about {pet['name']} it is a {pet['animal type']} the owner is {pet['owner']}")

#6-9. Favorite Places
favorite_places = {
    'sumanth': ['playground', 'hyderabad', 'nakrekal'],
    'prasad': ['dubai', 'bangkok'],
    'srikanth': ['singapore', 'malasia', 'thailand'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

#6-10. Favorite Numbers
favorite_numbers = {
    'srikanth': [9, 99],
    'prasad': [7, 45],
    'hari': [45, 22]
}

for name, fav_numbers in favorite_numbers.items():
    print(f"\n{name} likes the following numbers:")
    for number in fav_numbers:
        print(f"\t{number}")

#6-11. Cities
# Santiago is in Chile.
#   It has a population of about 6158080.
#   The Andes mountains are nearby.

# Kathmandu is in Nepal.
#   It has a population of about 1003285.
#   The Himilaya mountains are nearby.

# Talkeetna is in Alaska.
#   It has a population of about 876.
#   The Alaska Range mountains are nearby.
cities = {
    'kashmir': {
        'country': 'india',
        'population':  2158080,
        'near by mountains': 'himalaya',
    },
    'khatmandu': {
        'country': 'nepal',
        'population': 1003285,
        'near by mountains': 'himalaya',
    },
    'santigo': {
        'country': 'chile',
        'population': 6158080,
        'near by mountains': 'andes',
    },
}

for city, city_info in cities.items():
    # country = f"{city_info['country'].title()}"
    print(f"\n{city.title()} is in {city_info['country'].title()}.")
    mountain = f"{city_info['near by mountains']}"
    people = f"{city_info['population']}"
    print(f"\tit has a population of about {people}")
    print(f"\tThe {mountain.title()} mountains are near by")
