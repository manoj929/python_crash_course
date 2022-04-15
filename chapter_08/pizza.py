#Passing an Arbitrary Number of Arguments
# The asterisk in the parameter name *toppings tells Python to make an
# empty tuple called toppings and pack whatever values it receives into this tuple
# Note that Python packs the
# arguments into a tuple, even if the function receives only one value
def make_pizza(*toppings):
    """summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peas', 'extra cheese')

# mixing positional and arbitrary arguments
#Python assigns the first value it receives to the parameter size .
# All other values that come after are stored in the tuple toppings
def make_pizza(size, *toppings):
    """summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, 'pepperoni')
make_pizza(14, 'mushroom', 'extra cheese', 'sausage')