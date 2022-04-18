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
print()
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

    # modify attribute value through a method
    def update_odometer(self, mileage):
        """
        set the odometer reading to given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"you can't roll back on odometer!")
    
    #increment attribute value in method
    def increament_odometer(self, miles):
        """Add the given amount to odometer reading"""
        # self.odometer_reading += miles
        if miles >= 1:
            self.odometer_reading += miles
        else:
            print("you can't roll back on odometer")
    
my_new_car = Car('bmw', 'X5', 2021)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# modifying attribute's value directly
print()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print()
#modifying attributes value through a method
my_new_car.update_odometer(25)
my_new_car.read_odometer()

#printing on checking condition
my_new_car.update_odometer(28)
my_new_car.read_odometer()
print()

#incrementing attributes value through a method
my_used_car = Car('audi', 'a6', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increament_odometer(100)
my_used_car.read_odometer()