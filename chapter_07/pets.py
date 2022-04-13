# removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# try it yourself
#7-8 deli 'veggie', 'grilled cheese', 'turkey', 'roast beef'
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef', 'chicken sandwich',
    'pastrami', 'big mac', 'whopper burger']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    #making sandwich
    print(f"i'm working on your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)

print('\nfinished sandwiches are: ')
#print all sandwich made
for finished_sandwich in finished_sandwiches:
    print(f"i made a {finished_sandwich.title()}.")

#7-9 no pastrami
sandwich_orders = ['pastrami', 'veggie', 'grilled cheese', 'pastrami', 'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []
print("\ni'm sorry we're all run out of pastrami today!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"im making {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)
print('\n----sandwiches prepared-----')
for finished_sandwich in finished_sandwiches:
    print(f"i made {finished_sandwich.title()} sandwich.")

#7-10 dream vaccation name_prompt = "\nWhat's your name? "
# place_prompt = "If you could visit one place in the world, where would it be? "
# continue_prompt = "\nWould you like to let someone else respond? (yes/no) "
name_prompt = "\nwhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nwould you like to someone else respond? (yes/no) "
dream_vacation = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    dream_vacation[name] = place

    repeat = input(continue_prompt)
    if repeat != 'yes':
        break
print('\n------------')
#display the user poll
for name, place in dream_vacation.items():
    print(f"{name.title()}, would like to visit {place.title()}.")
