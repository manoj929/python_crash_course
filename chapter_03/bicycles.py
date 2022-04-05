bicycles = ['atlas', 'trek', 'hero', 'cannondale']
print(bicycles)
#accessing individual element in list
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[2])
print(bicycles[3])

bikes = ['r15', 'fz', 'ninja300', 'apache', 'vulcan']
#accessing last element in list
print(bikes[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

names = ['al karizmi', 'albert einstein', 'stephein hawking']
greetings = 'is genius'
print(f"{names[0]}, {greetings}")
print(f"{names[1]}, {greetings}")
print(f"{names[2]}, {greetings}")

cars = ['skoda slavia', 'honda city', 'hyundai verna', 'ciaz', 'xuv300']
print(f"I would like to own a {cars[0].title()}")