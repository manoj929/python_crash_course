
#10-6

while True:
    try:
        first_num = input("give me a number: ")
        if first_num == 'q':
            break

        first_num = int(first_num)

        second_num = input("give me another number: ")
        if second_num == 'q':
            break

        second_num = int(second_num)

    except ValueError:
        print("Sorry, I really needed a number.")
    else:
        sum = first_num + second_num
        print(f"The sum of {first_num} and {second_num} is {sum}")

#10-8 10-9
print()

filenames = ['chapter_10/text_files/cats.txt', 'chapter_10/text_files/dog.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            content = f.read()

    except FileNotFoundError:
        pass
        # print(f"sorry file {filename} is not there!")s
    else:
        print(content)

#10-10
print()

def count_word(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        pass

    else:
        word_count = content.lower().count('the')
        msg = f"'the' appears in alice.txt about {word_count} times."
        print(msg)

filename = 'chapter_10/text_files/alice.txt'
count_word(filename)
