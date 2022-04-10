# dictionaries
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#alien shot down
new_points = alien_0['points']
print(f"you just earned {new_points} points!")

#adding new key value pairs to dictionary
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#starting with an empty dictionary
alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 10
print(alien_1)
print()
#modifying values in dictionary
print(f"The allien is {alien_1['color']}")
alien_1['color'] = 'red'
print(f"The allien is now {alien_1['color']}")
print()
#moving alien
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#moving alien to the right
#determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be fast alien
    x_increment = 3
# the new position is old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
print()
# Remove key value pairs
# note: deleted key value pair is deleted permanently
alien_2 = {'color': 'blue', 'points': 10, 'speed': 'medium'}
print(alien_2)

del alien_2['speed']
print(alien_2)