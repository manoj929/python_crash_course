import json

#10-11
filename = "chapter_10/favorite_number.json"

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("what is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print(f"i know your favorite number it is {number}")