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