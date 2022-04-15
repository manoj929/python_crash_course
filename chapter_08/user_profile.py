# using arbitrary keyword arguments
# The double asterisks before the parameter **user_info cause Python to create an empty dictionary
def build_user(first, last, **user_info):
    """build a dictionary containing everything we know about user"""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_user('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)