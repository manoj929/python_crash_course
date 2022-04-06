#for loops
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f'{magician.title()} that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}\n")
    
print("Thank you for everyone. that was a great magic show!")

# avoiding indentation errors
#forgotten to indent line
singers = ['shreya goshal', 'thaman', 'anirudh']

# for singer in singers:
# print(singer)

# forgotten to indent additional lines
# code unexpected result
# this is a logical error second print statement should print once for each singer
for singer in singers:
    print(f"{singer.title()} your songs are great")
print(f"i can't wait for your next song, {singer.title()}")

# indenting unnecessarily (indentation error: unexpected indent)
# message = 'hello python world!'
#     print(message)

#indenting unnecessarily after loop cause to logical errors
#3rd printt() statement should print only once
dancers = ['shekar', 'jani', 'yash', 'pandu']
for dancer in dancers:
    print(f"{dancer.title()}, that was a great performance")
    print(f"I can't wait to see your next performance {dancer.title()}")

    print(f"\nThank you every one that was a great dance show")

#syntax error (: is must after for statement)
# bikes = ['pulsar', 'apache', 'fz']
# for bike in bikes
#     print(bike)