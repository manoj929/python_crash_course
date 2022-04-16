class Dog:
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate rolling over in respond to a command."""
        print(f"{self.name} rolled over.")

my_dog = Dog('willie', 7)
your_dog = Dog('Lucy', 4)
print(f"my dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.") 
my_dog.sit()

print(f"\nyour dog's name is {your_dog.name}.")
print(f"your dog is {your_dog.age} years old.")
your_dog.roll_over()

print('\n-----try it yourself-----')
# try it yourself
#9-1
class Restaurant:
    """A class representing a restaturant"""

    def __init__(self, name, causine_type):
        """initialize the restaurant"""
        self.name = name
        self.causine_type = causine_type
    
    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        if self.causine_type == 'sandwich':
            print(f"The {self.name} serves tasty {self.causine_type}")
        else:
            print(f"The {self.name} serves spicy and tasty {self.causine_type}")

    def open_restaurant(self):
        """display a message that the restaurant is open"""
        print(f"The {self.name} is open now, come on in!")

restaurant = Restaurant('shadab', 'Dum Biryani')
print(restaurant.name)
print(restaurant.causine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2 three restaurants
print('\n---three restaurant---')
sohail = Restaurant('sohail', 'paya soup')
sohail.describe_restaurant()

kritunga = Restaurant('kritunga', 'sea food')
kritunga.describe_restaurant()

tipsy_topsy = Restaurant('tipsy topsy', 'sandwich')
tipsy_topsy.describe_restaurant()

#9-3 users
print('\n----9-3-----')
class User:
    """class representing a user"""
    def __init__(self, first_name, last_name, username, mail, location):
        """initialize the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.mail = mail
        self.location = location
    
    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n {self.first_name} {self.last_name}:")
        print(f"\tusername: {self.username}\n\tEmail: {self.mail}\n\tLocation: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

rohith = User('rohith', 'shetty', 'r_shetty', 'rohit_sh@example.com', 'mumbai')
rohith.describe_user()
rohith.greet_user()

vijay = User('vijay', 'reddy', 'vijay_re', 'vijay_94@abc.com', 'hyderabad')
vijay.describe_user()
vijay.greet_user()