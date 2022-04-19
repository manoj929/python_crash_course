#importin a single class from module
# from car import Car
#importimg multiple classes from a module
# from car import Car, ElectricCar

#importin an Entire module
import car

# my_new_car = Car('audi', 'A4', '2022')
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

#work with import multiple classes
# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2020)
# print(my_tesla.get_descriptive_name())

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2020)
print(my_tesla.get_descriptive_name())