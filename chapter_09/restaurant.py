class Restaurant:
    """A class representing a restaturant"""

    def __init__(self, name, causine_type):
        """initialize the restaurant"""
        self.name = name
        self.causine_type = causine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"The {self.name} serves spicy and tasty {self.causine_type}")  

    def open_restaurant(self):
        """display a message that the restaurant is open"""
        print(f"The {self.name} is open now, come on in!")
    
    def set_number(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served
    
    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served
