# filling a dictionary with poll
responses = {}
#set a flag to indicate that polling is active
polling_active = True
while polling_active:
    #prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #store response in the dictionary
    responses[name] = response

    #find out if anyone else is going to take the poll
    repeat = input("would you like to let another person to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# polling is complete, show the results
print("\n-----Poll Results-----")
for name, response in responses.items():
    print(f"{name.title()}, would you like to climb {response.title()}")