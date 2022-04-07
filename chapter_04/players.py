#slicing a list
players = ['ronaldo', 'messi', 'virat kohli', 'michael jordan', 'florence']
print(players[0:3])

print(players[1:4])
#If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list
print(players[:3])

# if you want all items from the third item through the last item
print(players[2:])

# to output last three players
print(players[-3:])

# to skip items between a list
print(players[0:4:2])

#looping through a slice
fighters = ['mike tyson', 'jackie chan', 'bruce lee', 'tonyjaa', 'jet lee']

for fighter in fighters[:3]:
    print(fighter.title())