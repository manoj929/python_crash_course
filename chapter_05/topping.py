requested_toppings = ['mushrooms', 'extra cheese']
#Testing multiple conditions
if 'mushrooms'in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
print('\nFinished making pizza!')
print()

#logical error (it skips the next conditionals if one is correct)
if 'mushrooms'in requested_toppings:
    print('Adding mushrooms.')
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
print('\nFinished making pizza!')
print()

#alien color#1
# try it yourself
alien_color = 'green'
if alien_color == 'green':
    print('you just earned 5 points!')
alien_color = 'yellow'
if alien_color == 'yellow':
    print('you just earned 5points for yellow')
    alien_color = 'blue'
if alien_color == 'red':
    print('you just earned 10 points')

#alien colors#2
# if-else chain
alien_color = 'yellow'
if alien_color == 'green':
    print('you just earned 5 points.')
else:
    print('you earned 10 points')

print()
#alien colors#3
alien_color = 'red'
if alien_color == 'green':
    print('you just earned 5 points.')
elif alien_color == 'yellow':
    print('you just earned 15 points.')
else:
    print('you just earned 15 points.')

print()
#5-6 stages of life
age = 25
if age < 2:
    print("you're a baby")
elif age < 4:
    print("you're a toddler")
elif age < 13:
    print("you're a kid")
elif age < 20:
    print("you're a teenager")
elif age < 65:
    print("you're adult")
else:
    print("you're a elder")

print()

#5-7 favourite fruit
favourite_fruits = ['grapes', 'banana', 'gua']
if 'kiwi' in favourite_fruits:
    print('you really like kiwi')
if 'banana' in favourite_fruits:
    print('you really like banana!')
if 'gua' in favourite_fruits:
    print('you really like gua')
if 'dragon' in favourite_fruits:
    print('you really like grapes')
if 'apple' in favourite_fruits:
    print('you really like apple!')
