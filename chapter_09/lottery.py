from random import choice

def get_winning_ticket(possibilites):
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(possibilites)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    
    #we must have a winning ticket
    return True

def make_random_ticket(possibilites):
    ticket = []

    while len(ticket) < 4:
        pulled_item = choice(possibilites)
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket

possibilites = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
winning_ticket = get_winning_ticket(possibilites)

plays = 0
win = False

max_tries = 50_000

while not win:
    my_ticket = make_random_ticket(possibilites)
    win = check_ticket(my_ticket, winning_ticket)
    plays += 1

    if plays >= max_tries:
        break

if win:
    print("we have a winning ticket!")
    print(f"your_ticket: {my_ticket}")
    print(f"winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner:")
    print(f"your ticket: {my_ticket}")
    print(f"winning ticket: {winning_ticket}")