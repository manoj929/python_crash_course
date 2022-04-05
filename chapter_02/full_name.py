#using variables in strings
first_name = 'manoj'
last_name = 'reddy'
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"hello, {full_name.title()}")

message = f"Hello, {full_name.title()}"
print(message)

# To add a new line in a string
print("Languages:\nPython\nC\nJavascript")

# combine tabs and newlines in a single string
print("Languages:\n\tPython\n\tC++\n\tJava\n\tC#")

#stripping whitespace
#stripping rightspace
favourite_language = 'python  '
favourite_language = favourite_language.rstrip()

#remove white space from left side
programing_language = ' C++'
programing_language = programing_language.lstrip()

#remove whitespaces from bothsides
style_sheet = ' css '
style_sheet = style_sheet.strip()

print(favourite_language)
print(programing_language)
print(style_sheet)