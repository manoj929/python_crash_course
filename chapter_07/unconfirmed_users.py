# moving items from one list to another
unconfirmed_users = ['sandeep', 'naveen', 'peter']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"verifying user: {current_user.title()}")
    #adding to confirmed users
    confirmed_users.append(current_user)

#display all confirmed users
print(f"\nThe following users has been confirmed:")
for confirmed_user in confirmed_users:
    print(f"{confirmed_user.title()}")