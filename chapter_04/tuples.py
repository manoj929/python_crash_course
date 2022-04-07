# create tuples tuple
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
for dimension in dimensions:
    print(dimension)