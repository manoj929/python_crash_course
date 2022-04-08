# test using == operator
car = 'Audi'
condition = True
if car == 'audi':
    print(f'your guess is {condition}')
else:
    print(f'your guess is {condition != condition}')

if car.lower() == 'audi':
    print(f'your guess is {condition}')
else:
    print(f'your guess is {condition != condition}')

# checking equality and inequality
age = 20
has_licence = False
if age > 19:
    print('you are eligible')
if age < 19:
    print('you are not eligible')
if age >= 20:
    print('you are welcome to party')
if age <= 19:
    print('you are not allowed to party')

if age >= 20 and has_licence:
    print('you can drive the car')
else:
    print('you should not drive the car')

if age >= 20 or has_licence != True:
    print('you can drive the bike')

# test wether item in list 
available_fruits = ['apples', 'bananas', 'grapes', 'pineapple']
juice_item = 'pineapple'
if juice_item in available_fruits:
    print(f'making your {juice_item} juice')

#test wether item is not in list
juice_item = 'kiwi'
if juice_item not in available_fruits:
    print('sorry we dont have that fruit')

