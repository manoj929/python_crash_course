# if conditions 
cars = ['audi', 'bmw', 'maruti', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    
print()
#checking equality
bike = 'Honda'
print(bike == 'yamaha')
# if case matters it is advantage
print(bike == 'honda')
# if case doesn't matter ignoring case when checking equality
print(bike.lower() == 'honda')