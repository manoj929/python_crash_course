# store information about pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}

#summarizing the order
print(f"you ordered a {pizza['crust']}-crust pizza"
    "with the following toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)

#looping in loop
favorite_languages = {
    'sarah': ['c'],
    'jenny': ['python', 'ruby'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    #check the person has morethan one fav lang if it has (are) else (print :is)
    if len(languages) > 1:
        print(f"\n{name.title()}'s favourite languages are:")
    else:
        print(f"\n{name.title()}'s favourite language is:")
    for language in languages:
        print(f"\t{language.title()}")