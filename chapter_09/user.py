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
