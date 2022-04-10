# using get() to access values
alien_no_points = {
    'color': 'green',
    'speed': 'slow',
}
# showing a key error
# print(alien_no_points['points'])

point_value = alien_no_points.get('points', 'no points assigned')
print(point_value)
#If you leave out the second argument in the call to get() and the key doesn’t exist,
# Python will return the value None . The special value None means “no value exists.”
# This is not an error: it’s a special value meant to indicate the absence of a value.
print()
# try it yourself
person = {
    'first_name': 'thomas',
    'last_name': 'shelby',
    'age': 30,
    'city': 'bhirminghum'
}

print(person['first_name'])
print(person['last_name'])
print(person.get('age', 42))
print(person['city'])

# 6-2 favorite-numbers
favorite_numbers = {
    'sumanth': 5,
    'raju': 9,
    'naveen': 7,
    'srinu': 5,
    'riyaz': 7,
}

num = favorite_numbers['sumanth']
print(f"Sumanth's favorite number is: {num}")

num = favorite_numbers['raju']
print(f"Raju favorite nuber is: {num}")

num = favorite_numbers['naveen']
print(f"naveen favorite nuber is: {num}")

num = favorite_numbers['srinu']
print(f"Srinu favorite nuber is: {num}")

num = favorite_numbers['riyaz']
print(f"Riyaz favorite nuber is: {num}")

print()
#6-3 glossary
glossary = {
    'string': 'A series of characters',
    'comment': 'A note in a program that python interpreter ignores',
    'list': 'A collection of items in a particular order',
    'loop': 'work through a collection of items, one at a time',
    'dictionary': 'a collection of key-value pairs',
}

word = 'string'
print(f"{word.title()}: {glossary['string']}")

word = 'comment'
print(f"\n{word.title()}: {glossary['comment']}")

word = 'list'
print(f"\n{word.title()}: {glossary['list']}")

word = 'loop'
print(f"\n{word.title()}: {glossary['loop']}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary['dictionary']}")