requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"adding {requested_topping}")
print(f"\nFinished making your pizza!")
print()
#But what if the pizzeria runs out of green peppers?
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('sorry we are run out of green peppers right now')
    else:
        print(f"adding {requested_topping}")
print(f"\nFinished making your pizza!")
print()
# Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want plain pizza!")
print()
# using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
user_requested = ['mushrooms', 'french fries', 'extra cheese']

for user_request in user_requested:
    if user_request in available_toppings:
        print(f"Adding {user_request}")
    else:
        print(f'sorry we dont have {user_request}')
print("\nFinished making pizza!")