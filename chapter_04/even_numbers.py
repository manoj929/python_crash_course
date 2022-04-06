even_numbers = list(range(2, 11, 2))
print(even_numbers)

#squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#same example omit temporary variable
# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
# print(squares)

#simple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
#sum all the numbers in list
print(sum(digits))

#same example from squares but it done in one line code
#list comprehension
square_numbers = [value**2 for value in range(1, 11)]
print(square_numbers)