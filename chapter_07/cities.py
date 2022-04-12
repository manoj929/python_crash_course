#using break to exit a loop
prompt = '\nplease enter ciy you have visited:'
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"i'd love to go to {city.title()}!")