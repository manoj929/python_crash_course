#find the number is even or odd
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

#try it yourself
#7-1 Rental car
rental_car = input('what kind of car would you like to rent? ')
print(f'\nlet me find you a {rental_car}')

#7-2restaurent seating
seating = input("how many people are there in your dinner group? ")
seating = int(seating)

if seating > 8:
    print(f"\nyou have to wait for a table.")
else:
    print(f"\nyour table is ready.")

#multiple of ten
num = input('give a number please: ')
num = int(num)

if num % 10 == 0:
    print(f"{num} is a multiple of 10")
else:
    print(f"{num} is not a multiple of ten")