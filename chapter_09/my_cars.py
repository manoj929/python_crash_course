from car import Car
#using aliases
from electric_cars import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', 2020)
print(my_tesla.get_descriptive_name())