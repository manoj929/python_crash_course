"""A set of classes used to represent gas and electric cars."""

class Car:
    """A simple attempt to represent a car."""

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

    def update_odometer(self, mileage):
        """
        set the odometer reading to given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"you can't roll back on odometer!")
    
    def increament_odometer(self, miles):
        """Add the given amount to odometer reading"""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery from an electric car."""

    def __init__(self, battery_size=75):
        """Initialize battery attribut"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def get_range(self):
        """print a statement about the range this battery povides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on full charge.")

class ElectricCar(Car):
    """Models aspects of a car, specific to Electric vehicles"""

    def __init__(self, make, model, year):
        """
        initialize attributes of parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()