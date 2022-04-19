"""A car that can be used to represent car."""

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