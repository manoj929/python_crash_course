#passing list to function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['candy', 'billie', 'eminem']
greet_users(usernames)