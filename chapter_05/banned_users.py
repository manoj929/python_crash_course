# checking whether a value is not in list
banned_users = ['andrew', 'carolina', 'david']
user = 'jennie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# try it yourself
car = True
car_model = 'jaguar'


if car == 'lamborgini':
    print(f'yes it is the {car}')


if car_model == 'scorpio':
    print(f"yes it is {car}")
elif car_model == 'fortuner':
    print(f"yes it is {car}")
elif car_model == 'xuv':
    print(f"yes it is {car}")
elif car_model == 'safari':
    print(f"yes it is {car}")
elif car_model == 'range rover':
    print(f"yes it is {car}")
elif car_model == 'jeep':
    print(f"yes it is {car}")
elif car_model == 'jaguar':
    print(f"yes it is {car}")
else:
    print('your car doesnt match with the any of the options')