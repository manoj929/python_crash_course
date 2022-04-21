filename = 'chapter_10/learning_python.txt'
#10-1
print("--- Reading in the entire file:")
with open(filename) as file_object:
    content = file_object.read()
print(content)

print("\n--- Looping over the lines:")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
    
print("\n--- Storing the lines in a list:")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

#10-2learning-c
print()
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip().replace('Python', 'C')
    print(line)

#10-3
# print()
# file_path = 'chapter_10/guest.txt'
# name = input('Enter your name: ')

# with open(file_path, 'w') as file_object:
#     file_object.write(name)

# #10-4
# print()
# file_path = 'chapter_10/guest_book.txt'

# print("Enter 'quit' when you are finished.")
# while True:
#     name = input("what's your name? ")
#     if name == 'quit':
#         break
#     else:
#         with open(file_path, 'a') as file_object:
#             file_object.write(name + '\n')
#             print(f"Hi {name}, you've been added to the guest book") 

#10-5
print()
# Why do you like programming? Programmers can build almost anything they can imagine.
# Would you like to let someone else respond? (y/n) y

# Why do you like programming? It's really fun, and really satisfying.
# Would you like to let someone else respond? (y/n) y

# Why do you like programming? It just never gets old.
# Would you like to let someone else respond? (y/n) n

filename = 'chapter_10/programing_poll.txt'
responses = []
while True:
    response = input("why do you like programming? ")
    responses.append(response)

    continue_poll = input("would you like to let someone else respond? (y/n)")
    if continue_poll != 'y':
        break
    else:
        with open(filename, 'a') as file_object:
            for response in responses:
                file_object.write(response  + '\n')