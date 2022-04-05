guests = ['prabhas', 'ntr', 's.s.rajamouli',]
print(f"Hello mr {guests[0].title()} inviting you as a chief guest for event")
print(f"Hello mr {guests[1].title()} inviting you as a chief guest for event")
print(f"Hello mr {guests[2].title()} inviting you as a chief guest for event")

busy_guest = 'prabhas'
guests.remove(busy_guest)
print(f"{busy_guest.title()} is busy in shoot so he can't attend the event")

guests.insert(0, 'ram charan')
print(f"Hello mr {guests[0].title()} inviting you as a chief guest for event")
print(f"Hello mr {guests[1].title()} inviting you as a chief guest for event")
print(f"Hello mr {guests[2].title()} inviting you as a chief guest for event")

# adding more guests
guests.insert(0, 'Rana')
guests.insert(2, 'chiranjeevi')
guests.append('Nani')
print(f"{guests[0].title()} is attending the event")
print(f"{guests[1].title()} is attending the event")
print(f"{guests[2].title()} is attending the event")
print(guests)

# print inviting only two guests
print(f'i inviting {guests[2].title()} and {guests[4].title()} for the event')

removed_guest = guests.pop()
print(f"excuse me for not inviting you to event {removed_guest.title()}")
print(f"{guests.pop(0).title()} excuse me for not inviting you to event")
print(f"{guests.pop(2).title()} excuse me for not inviting you to event")
print(f"{guests.pop(0).title()} excuse me for not inviting you to event")

print(f"{guests[0].title()} is attending the event")
print(f"{guests[1].title()} is attending the event")

del guests[0]
del guests[-1]
print(guests)