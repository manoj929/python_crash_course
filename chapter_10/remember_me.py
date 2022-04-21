import json

username = input("What is your name? ")

filename = "chapter_10/username.json"
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"we'll remember you when you come back, {username}")