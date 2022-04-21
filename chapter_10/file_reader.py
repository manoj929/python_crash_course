filename = 'chapter_10/text_files/pi_digits.txt'

with open('chapter_10/pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

#making a list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())