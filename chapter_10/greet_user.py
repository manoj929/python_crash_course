import json

filename = "chapter_10/username.json"
with open(filename) as f:
    username = json.load(f)
    print(f"welcome back {username}")