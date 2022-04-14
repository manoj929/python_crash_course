# try it yourself
#8-3 t-shirt
def make_tshirt(size, message):
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f"It will say, {message}")
make_tshirt('large', 'Ilove python!')
make_tshirt(message = 'Readibility counts', size = 'medium')

#8-4 modify default values
def make_shirt(size = 'large', message = 'I love python'):
    print(f"\nIm going to make a {size} shirt")
    print(f"it will say {message}")
make_shirt()
make_shirt('medium')
make_shirt('small', 'programmers are loopy.')

#8-5 cities
def describe_city(city, country = 'India'):
    print(f"\n{city} is in {country}.")
describe_city('chennai')
describe_city('sydney',  'Australia')
describe_city('hyderabad')