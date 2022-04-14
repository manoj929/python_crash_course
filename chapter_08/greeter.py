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