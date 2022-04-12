# try it yourself
#7-4 pizza toppings
prompt = '\nWhat topping would you like on your pizza?'
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza")

#7-5 movie tickets
prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' when you are finished: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('your ticket is free')
    elif age < 12:
        print('your ticket is $10')
    else:
        print('your ticket is $15')

#7-6 three exits
prompt = '\nWhat topping would you like on your pizza?'
prompt += "\nEnter 'quit' when you are finished: "
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I will add {topping} to your pizza")

#another example
prompt = "\nEnter your age? "
prompt += "\nEnter 'quit' when you are finished: "
activate = True
while activate:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('your ticket is free')
    elif age < 12:
        print('your ticket is $10')
    else:
        print('your ticket is $15')
