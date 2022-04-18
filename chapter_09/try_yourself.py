#9-4 number served
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

restaurant = Restaurant('spicy hub', 'shawarma')
restaurant.describe_restaurant()

print(f"Number served: {restaurant.number_served} customers")
restaurant.number_served = 430
print('number served:' + str(restaurant.number_served) + ' customers')

restaurant.set_number(1257)
print(f"Number served: {restaurant.number_served} customers")

restaurant.increment_number_served(240)
print(f"Number served in a day: {restaurant.number_served} customers")


#9-5 login attempts
print('\n----9-5-----')
class User:
    """class representing a user"""
    def __init__(self, first_name, last_name, username, mail, location):
        """initialize the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.mail = mail
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n {self.first_name} {self.last_name}:")
        print(f"\tusername: {self.username}\n\tEmail: {self.mail}\n\tLocation: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attements(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


abhi = User('abhinav', 'gomatam', 'abhi_gomatam', 'abhinav@abc.com', 'hyderabad')
abhi.describe_user()
abhi.greet_user()

print('\nmaking login attemts')
abhi.increment_login_attements()
abhi.increment_login_attements()
abhi.increment_login_attements()
print(f"Login attempts: {abhi.login_attempts}")

print(f"Resetting login attemps")
abhi.reset_login_attempts()
print(f"Login attempts: {abhi.login_attempts}")