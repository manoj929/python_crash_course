#modifying elements in list
bikes = ['yamaha', 'honda', 'suzuki']
print(bikes)

bikes[1] = 'ducati'
print(bikes)

# addin elements to list
# appending element to end in list
bikes.append('honda')
print(bikes)

motorcycles = []
motorcycles.append('kawasaki')
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('pulsar')
print(motorcycles)

# inserting elements into a list
#you can add a new element at any position in your list by using insert() method
motorcycles.insert(0, 'yamaha')
motorcycles.insert(1, 'pulsar135')
print(motorcycles)

# removing an item in list using del statement
# you can remove an item from any position in a list using the del statement if you know its index.
#you can no longer access the deleted value
del motorcycles[3]
print(motorcycles)
del motorcycles[2]
print(motorcycles)

# remove an item using pop() method
# pop() removes item in end of list
cruiser_bike = ['avenger', 'entizer', 'meteor', 'thunderbird', 'harleydavidson']
print(cruiser_bike)

popped_bike = cruiser_bike.pop()
print(cruiser_bike)
print(popped_bike)

last_owned = motorcycles.pop()
print(f"The last bike i owned was a {last_owned.title()}")

#popping items from any position in a list
# you can use pop() to remove an item from any position in a list by including the index of the item you want to remove in paranthesis
first_owned = motorcycles.pop(1)
print(f"The first moorcycle i owned was a {first_owned.title()}")

# removing an item by value
sports_bike = ['R1', 'zx10r', 'ducati', 'gsx1000', 'hayabusa', 'cbr1000rr']
print(sports_bike)

sports_bike.remove('gsx1000')
print(sports_bike)

too_expensive = 'ducati'
sports_bike.remove(too_expensive)
print(sports_bike)
print(f"{too_expensive.title()} is too expensive bike for me.")

# The remove() method deletes only the first occurrence of the value you specify. If there’s
# a possibility the value appears more than once in the list, you’ll need to use a loop
# to make sure all occurrences of the value are removed. You’ll learn how to do this in Chapter 7