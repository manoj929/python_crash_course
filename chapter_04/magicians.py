#for loops
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f'{magician.title()} that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}\n")
    
print("Thank you for everyone. that was a great magic show!")