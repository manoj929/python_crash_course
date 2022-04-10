# try it yourself
glossaries = {
    'string': 'A series of characters',
    'comment': 'A note in a program that python interpreter ignores',
    'list': 'A collection of items in a particular order',
    'loop': 'work through a collection of items, one at a time',
    'dictionary': 'a collection of key-value pairs',
    'python': 'python is a great language and easy to use',
    'java': 'java is great for web, mobile and enterprise application development',
    'php': 'it is widely used for web applications and easy to learn',
    'ruby': 'ruby also used for backend web applications and simple to use',
    'rust': 'rust is a new programing language and best performance'
}

for word, meaning in glossaries.items():
    print(f"\n{word.title()}: {meaning.title()}")
print()
#6-5 rivers
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()}, runs through {country.title()}\n")

for river in rivers.keys():
    print(river.title())
print()
# print each country in rivers dictionary
for country in rivers.values():
    print(country.title())
print()
#6-6 poll
favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'java',
    'mike' : 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is: {language.title()}")

coders = ['edward', 'maya', 'ram', 'sarah', 'jonas', 'hitesh']
print()
for coder in coders:
    if coder in favorite_languages:
        print(f"Thank you for taking the poll {coder.title()}")
    else:
        print(f"{coder.title()}, what is your favorite language?")