#using break to exit a loop
prompt = '\nplease enter ciy you have visited:'
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"i'd love to go to {city.title()}!")

#using continue in while loop
#continue skips based on condition(prints only the odd numbers in that range)
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)

#avoid infinite loop
# x =1
# while x <= 5:
#     print(x)