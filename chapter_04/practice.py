counting_to_20 = []
for index in range(1, 21):
    counting_to_20.append(index)
print(counting_to_20)

# sending one million numbers to list
one_million = []
for index in range(1, 1000001):
    one_million.append(index)
# print(one_million)

#find minimum number in one million
print(min(one_million))
#find maximum number in one million
print(max(one_million))

#adding one million numbers using sum()
print(sum(one_million))

# print odd numbers
odd_numbers = []
for i in range(1, 11, 2):
    odd_numbers.append(i)
print(odd_numbers)
# short code
odd = list(range(1,20,2))
print(odd)

#multiples of three
threes = []
for value in range(3, 31):
    if value % 3 == 0:
        threes.append(value)
print(threes)

#single line code
threes_in_list = [value for value in range(3, 31) if value % 3 == 0]
print(threes_in_list)

#cubes
cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)
print(cubes)

#list comprehensions
cube = [num ** 3 for num in range(1, 11)]
print(cube)