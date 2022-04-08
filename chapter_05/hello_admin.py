# try it youself
# 5-8 hello admin
usernames = ['sara', 'john', 'admin', 'surli', 'mike']
for username in usernames:
    if username == 'admin':
        print(f"Hello {username} would you like to see a status report?")
    else:
        print(f"Hello {username} thank you for logging in again")

print()
# 5-9. No Users
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"hello admin would you like to see a status report?")
        else:
            print(f"hello {username}")
else:
    print('we need to find some users!')
print()
# 5-10. Checking Usernames
current_users = ['lasya', 'pradeep', 'ravi', 'Harish', 'harika']
new_users = ['suresh', 'lasya', 'kalyan',  'Prasad', 'RAVI', 'yogesh']

#convert all names to lowercase and append to list
# current_user_lower = []
# for user in current_users:
#     current_user_lower.append(user.lower())
# using list comprehenson for shot code
current_users_lower = [user.lower() for user in current_users]

#make sure comparision is case sensitive
#check the user name is available or not if it not available print if statement
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is already taken, choose another username!")
    else:
        print(f"{new_user} is available")

print()
# 5-11. Ordinal Numbers:
ordinal_numbers = list(range(1,10))
for number in ordinal_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f"{number}th")