from user import User


class Admin(User):
    def __init__(self, first_name, last_name, username, mail, location):
        super().__init__(first_name, last_name, username, mail, location)
        self.privileges = Privileges()
    
class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        print('\nprivileges')
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("-This user has no privilages.")
    