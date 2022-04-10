# nesting
# aliens_0 = {'color': 'green', 'points': 5}
# aliens_1 = {'color': 'yellow', 'points': 10}
# aliens_2 = {'color': 'red', 'points': 15}

# aliens = [aliens_0, aliens_1, aliens_2]

# for alien in aliens:
#     print(alien)

aliens = []
#make 30 green aliens
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#loop through a slice first three aliens to modify
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

#show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
print(aliens)