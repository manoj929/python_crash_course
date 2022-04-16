# using arbitrary keyword arguments
# The double asterisks before the parameter **user_info cause Python to create an empty dictionary
def build_user(first, last, **user_info):
    """build a dictionary containing everything we know about user"""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_user('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

#try it yourself
#8-12
def make_sandwich(*items):
    """make a sandwich with a given items"""
    print(f"\nI'll make a great sandwich:")
    for item in items:
        print(f"...adding {item} to your sandwich")
    print("your sandwich is ready")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')

#8-13
build_profile = build_user('van russum', 'guido', location = 'Netherlands', field = 'programmer', invented = 'python')
print('\n',build_profile)

#8-13
def make_car(manufacturer, model, **car_dict):
    """Make a dictionary representing a car"""
    car_dict['manufacturer'] = manufacturer
    car_dict['model'] = model

    return car_dict

car = make_car('Maruti', 'baleno', color='blue', tow_package=True)
print(car)
car = make_car('MG', 'hector', color = 'red', year=2020, feature='internet inside')
print(car)

#another way of above example
def build_car(manufacturing, model, **options):
    car_dict = {
        'manufacturer': manufacturing,
        'model': model,
    }

    for option, value in options.items():
        car_dict[option] = value
    
    return car_dict
    
car = build_car('honda', 'civic', color='white', year=2021)
print(car)
car = build_car('toyota', 'innova crysta', color='grey', country_0rigin='japan', utility='muv')
print(car)