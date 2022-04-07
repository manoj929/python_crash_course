# defining tuples
dimensions = (200, 50)
print(dimensions[0])

# tuples items cannot reassign
# dimensions[0] = 250
# print(dimensions[0])

#Tuples are technically defined by the presence of a comma If you want to define a tuple with one element
my_t = (43,)
print(type(my_t))
print(my_t)
print()
# looping through all values in a tuple
print('original dimensions')
for dimension in dimensions:
    print(dimension)

#writing over a tuple
dimensions = (400, 100)
print('\nmodified dimensions')
for dimension in dimensions:
    print(dimension)

print()
# try it your-self
buffet_menu = ('chicken biryani', 'shawarma', 'kababs', 'french fries', 'noodles')
print('try our menu')
for buffet in buffet_menu:
    print(buffet)

# tuples cannot change value
# buffet_menu[3] = 'paya soup'
# print(buffet)

buffet_menu = ('chicken biryani', 'shawarma', 'kababs', 'paya soup', 'chicken 65')
print('\nhere is our updated menu:')
for buffet in buffet_menu:
    print(buffet)