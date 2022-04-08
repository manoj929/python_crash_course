age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"your admission coast is ${price}")

# giving discounts for seniors adding one more elif
age = 40
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"your admission coast is ${price}")

#Omitting the else block
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age>= 65:
    price = 20
print(f"your admission coast is ${price}")