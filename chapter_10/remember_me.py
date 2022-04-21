import json

#load the username, if it has been stored previously.
# otherwise, primpt for the username and store it.
filename = "chapter_10/username.json"
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"we'll remember you when you come back, {username}")
else:
    print(f"welcome back {username}")