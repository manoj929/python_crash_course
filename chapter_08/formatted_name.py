# returning a simple value
def get_formatted_name(firstname, lastname):
    """return a fullname neatly formatted."""
    fullname = f"{firstname} {lastname}"
    return fullname.title()

# When you call a function that returns a value, you need to provide a
# variable that the return value can be assigned to. In this case, the returned
# value is assigned to the variable musician

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#making an argument optional
#If you specify a default value for a parameter, no spaces should be used on either side of the equal sign
#The same convention should be used for keyword arguments in function calls
def get_formatted_name(first_name, last_name, middle_name=''):
    """return a fullname neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print('\n'+musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)