class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel_tank_capacity = 45
    
    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"you can't roll back on odometer!")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print(f"This car has {self.fuel_tank_capacity}-litres of fuel tank capacity")
    
#instances as attributes
class Battery:
    """a simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):
        """Initialize the battery's attribute"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """print a statement about the range this provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicle"""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # self.battery_size = 75
        #instances as attributes
        self.battery = Battery()

    #defining attributes and methods for child class
    # def describe_battery(self):
    #     """Print a statement describing the battery size"""
    #     print(f"This car has a {self.battery_size}-kwh battery")
    
    #overriding methods from parent class
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\nMake an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\nupgraded the battery")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()