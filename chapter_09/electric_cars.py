"""A set of classes that can be used to represent electric cars."""
from car import Car

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