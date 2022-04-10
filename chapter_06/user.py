#loop through dictionary
user_0 = {
    'username': 'jefri',
    'firstname': 'jerico',
    'lastname': 'fermi'
}
# The second half of the for statement at 1 includes the name of the
# dictionary followed by the method items() , which returns a list of key-value
# pairs
for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

#looping 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['sarah', 'phil']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, i see you love {language}")

# the keys() is not just for looping : it actually returns a list of all the keys.
if 'erin' not in favorite_languages.keys():
    print('\nErin please take our pool')
print()
#looping through diictionary keys in a particular order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print()
#loop throuh all values in dictonary
for language in favorite_languages.values():
    print(language.title())
print()
#to see each language whithout repetation use set
#A set is a collection in which each item must be unique:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'mike': 'java',
    'phil': 'python'
}
print('The following languages have been mentioned')
for language in set(favorite_languages.values()):
    print(language.title())

# When you wrap set() around a list that contains duplicate items, Python
# identifies the unique items in the list and builds a set from those items
