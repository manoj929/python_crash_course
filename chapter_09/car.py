class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """return a neatly formatted name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())

#setting a default value for an attribute
class Car:
    
    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name
    
    def read_odometer(self):
        """print a statement showing car's mileage"""
        print(f"this car has {self.odometer_reading} miles  on it.")
    
my_new_car = Car('bmw', 'X5', 2021)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()