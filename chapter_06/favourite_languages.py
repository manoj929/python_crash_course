favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'java',
    'mike' : 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is: {language}.")
print()

#loop through dictionary
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is: {language.title()}")

#looping through all the keys in a dictionary (keys() easier to read)
for name in favorite_languages.keys():
    print(f"\n{name.title()}")

# or use any of one both works same for (displays keys only)
for name in favorite_languages:
    print(name.title())