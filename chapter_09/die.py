from random import randint

class Die:
    """Represent a die which can be rolled"""

    def __init__(self, sides=6):
        """Initialize the die"""
        self.sides = sides
    
    def roll_die(self):
        """return a number between 1 and number of sides"""
        return randint(1, self.sides)


# Make a 6-sided die, and show the results of 10 rolls.
dice_6 = Die()

results = []
for roll_num in range(10):
    result = dice_6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

dice_10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = dice_10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

dice_20 = Die(sides=20)
results = []

for roll_num in range(20):
    result = dice_20.roll_die()
    results.append(result)
print('\n10 rolls of a 20-sided die:')
print(results)