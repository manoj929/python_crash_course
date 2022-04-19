from random import choice

possibilites = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']

winning_prize = []

while len(winning_prize) < 4:
    pick_item = choice(possibilites)
    if pick_item not in winning_prize:
        print(f"we pick the choice: {pick_item}")
        winning_prize.append(pick_item)
print(winning_prize)