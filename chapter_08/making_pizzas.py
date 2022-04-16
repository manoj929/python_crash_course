# this approach available every function from the module
import pizza

#if we want to import just the (specific function)function we're going to use
# from pizza import make_pizza
# make_pizza(12, 'onion')
# make_pizza(14, 'extra cheese', 'honey')


pizza.make_pizza(12, 'pepperoni')
pizza.make_pizza(16, 'mushrooms', 'extra  cheese', 'sausage')

# Here we give the function make_pizza() an alias, mp() , by importing
# make_pizza as mp . The as keyword renames a function using the alias you provide
from pizza import make_pizza as mp

mp(10, 'ginger')

# Using as to Give a Module an Alias
import pizza as p

p.make_pizza(10, 'sausage')