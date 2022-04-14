#A Python docstring is a string used to document a Python module, class, function or method,
# so programmers can understand what it does without having to read the details of the implementation
# """Docstrings are enclosed in triple quotes."""
def greet_user():
    """Display a message"""
    print('Hello!')

greet_user()

#passing information to a function
def greet_user(username):
    print(f"hello {username.title()}")
greet_user('manoj')
greet_user('suresh')

# try it youself
#8-1 message
def display_message():
    print("Hi all i'm learning functions in this chapter")
display_message()

#8-2
def favorite_book(name):
    print(f"\n{name.title()} is One of my favorite book !")
favorite_book('python crash course')

#try it your self
#8-6
def city_country(city, country):
    city_in_country = f"{city.title()}, {country.title()}"
    return city_in_country

print("\n cities in countries")
india = city_country('hyderabad', 'India')
print(india)

pakistan = city_country('lahore', 'pakistan')
print(pakistan)

bangkok = city_country('bangkok', 'Thailand')
print(bangkok)

#8-7 album
def make_album(artist_name, album_title, songs = None):
    """Build a dictionary containing information about an album."""
    music_album = {'name': artist_name, 'title': album_title,}
    if songs:
        music_album['songs'] = songs
    return music_album

album = make_album('m.jackson', 'dangerous')
print(f"\n{album}")

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('iron maiden', 'piece of mind', songs=8)
print(album)

#user albums
print('\nEnter "quit" to exit at any time!')
while True:
    artist_name = input('\nplease enter artist name: ')
    if artist_name == 'quit':
        break
    album_title = input('please enter album title: ')
    if album_title == 'quit':
        break

    album = make_album(artist_name, album_title)
    print(album)

print('Thanks for responding!')