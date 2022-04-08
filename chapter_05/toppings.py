# checking for inequality
requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print('Hold the anchovies!')

# numerical comparision
answer = 20
if answer != 42:
    print('That is not correct answer please try again')

print()
#checking multiple conditions
# using and to check multiple conditions (if both true then only pass)
age_0 = 21
age_1 = 24

print(age_0 >= 21 and age_1 <=22)
# to improve readability use paranthesis
print((age_0 >= 21) and (age_1 >= 21))

print()
# using or to check multiple condition (when either or both of the individual tests pass)
# an (or) expression fails only when both the individual tests fail
person_1 = 21
person_2 = 18
print(person_1 >= 21 or person_2 >= 21)

person_1 = 18
print(person_1 >= 21 or person_2 >= 21)

print()

# checking wether a value is in a list using(in) keyword
toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in toppings)
print('pepperonion' in toppings)