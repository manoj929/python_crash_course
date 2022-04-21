import json

numbers = [2, 3, 5, 7, 9, 11, 13]

filename = 'chapter_10/numbers.json'
with open(filename, 'w') as fp:
    json.dump(numbers, fp)