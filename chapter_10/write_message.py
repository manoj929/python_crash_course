filename = 'chapter_10/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.')
    """
    If you want to store numerical data in a
    text file, you’ll have to convert the data to string format first using the str()
    """
    file_object.write("I love python programming." + str(143))
    #writing multiple lines
    file_object.write("I love creating games.\n")
    file_object.write('I love programming but\n')
    file_object.write('I don"t know what to create with it.\n')

#appending to a file
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large dataseta.\n")
    file_object.write("I love creating apps that run in browser.\n")