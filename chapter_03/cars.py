cars = ['bmw', 'audi', 'toyota', 'honda']
#sort() method will permanently sorts the order you can use sort(reverse=True) to reverse the order
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily with the sorted() function
sports_cars = ['buggati', 'lamorgini', 'ferrari', 'aston martin']
print('Here is the original list:')
print(sports_cars)

print('\nHere is the sorted  list:')
print(sorted(sports_cars))

print('\nHere is the original list again:')
print(sports_cars)

# printing list in reverse order
luxury_cars = ['rolce royce', 'bentley', 'range rover', 'mercedes']
print(luxury_cars)
luxury_cars.reverse()
#Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list
print(luxury_cars)
luxury_cars.reverse()
print(luxury_cars)

# print lenght of a list using len()
print(len(luxury_cars))