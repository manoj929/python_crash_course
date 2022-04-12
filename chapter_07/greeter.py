#multi line message
prompt = 'if you tell us who you are , we can personalize the message you see.'
prompt += '\nwhat is your first name? '
name = input(prompt)
print(f"\nHello {name}")

age = input("Hello what is your age? ")
print(age)
print(type(age))

age = int(age)
print(type(age))
print(age >= 18)