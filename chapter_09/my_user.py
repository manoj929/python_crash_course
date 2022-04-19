from admin import Admin

james = Admin('james', 'bond', 'james_bond', 'james_bond@abc.com', 'United Kingdom')
james.describe_user()
# james.privileges.show_privileges()
# print("\nadding privileges to user")
james_privileges = ['can edit post', 'can delete post', 'can create post', 'can suspend account']
james.privileges.privileges = james_privileges
print('\nThe admin james has these privileges:')
james.privileges.show_privileges()