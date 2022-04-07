# copying list
my_foods = ['pizza', 'biryani', 'ice cream']
friends_foods = my_foods[:]

print(f'My favourite foods are: \n {my_foods}')

print('\nMy friend"s favourite foods are:')
print(friends_foods)

#both list are seperate to proove
# adding seperate food items to each list
my_foods.append('juice')
friends_foods.append('thumpsup')

print(f'My favourite foods are: \n {my_foods}')

print('\nMy friend"s favourite foods are:')
print(friends_foods)

#this doesn't work both will display same
# friends_foods = my_foods
# This syntax actually tells Python to associate the new variable friend_foods with the list that is already associated with
# my_foods , so now both variables point to the same list. As a result, when we add 'cannoli' to my_foods , it will also appear
# in friend_foods . Likewise 'ice cream' will appear in both lists, even though it appears to be added only to friend_foods .
# The output shows that both lists are the same now, which is not what we wanted

# Try it yourself
# 4-10
cities = ['hyderabad', 'vizag', 'bangalore', 'rajmaundry', 'chennai']
print(cities[:3])
print(cities[1:4])
print(cities[-3:])
print()
#4-11
pizzas = ['chicken cheese', 'papper onion', 'marghareta']
friends_pizza = pizzas[:]

pizzas.append('veg pizza')
friends_pizza.append('italian pizza')

print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('\nMy friend favourit pizzas are:')
for pizza in friends_pizza:
    print(pizza)