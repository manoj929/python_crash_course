#passing list to function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['candy', 'billie', 'eminem']
greet_users(usernames)

#try it yourself
#8-9 messages
def show_messages(messages):
    """print each text message"""
    print('\n')
    for message in messages:
        print(message)

greetings = ["hello there", "how are u?", ":)"]
show_messages(greetings)

#8-10 sending messages
def show_messages(messages):
    """print each text message"""
    print('\nsent messages...')
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """print each message and move it to sent message"""
    while messages:
        current_message = messages.pop()
        print(f"sending... {current_message}")
        sent_messages.append(current_message)

greetings = ["hello there", "how are u?", ":)"]
sent_messages = []
print('----8-10-----')
send_messages(greetings, sent_messages)
show_messages(sent_messages)

print('\nfinal list')
print(greetings)
print(sent_messages)

#8-11 archived messsages
def show_messages(messages):
    """print each text message"""
    print('\nshowing all messages...')
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """print each message and move it to sent message"""
    while messages:
        current_message = messages.pop()
        print(f"sending... {current_message}")
        sent_messages.append(current_message)

greetings = ["hello there", "how are u?", "what u doing"]
print('\n----8-11-----')
show_messages(greetings)

sent_messages = []
send_messages(greetings[:], sent_messages)

print('\nfinal lists')
print(greetings)
print(sent_messages)