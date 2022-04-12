# #input() method
message = input('Tell me something: ')
print(message)

#writing clear prompts
name = input('please enter you name: ')
print(f"\nHello {name}!")

prompt = '\nTell me something, and i will repeat it back to you:'
prompt += '\nEnter quit to end the program. '

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)