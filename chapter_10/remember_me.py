import json

def get_stored_username():
    """Get stored username if available"""
    filename = "chapter_10/username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """prompt for a new username"""
    username = input("what is your name? ")
    filename = "chapter_10/username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username
    
def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username} (y/n): ")
        if correct == 'y':
            print(f"welcomeback {username}!")
        else:
            username = get_new_username()
            print(f"we'll rememeber you when you comeback again {username}.")
    else:
        username = get_new_username()
        print(f"we'll remember you when you come back, {username}.")
        

greet_user()