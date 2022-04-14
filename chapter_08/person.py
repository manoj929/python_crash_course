# returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimmi', 'handrix')
print(musician)

#
def build_person(first_name, last_name, age = None):
    """Return a dictionary of information about person."""
    person = {'first': first_name, 'last': last_name,}
    if age:
        person['age'] = age
    return person

musician = build_person('jimmi', 'handrix', 25)
print(musician)

#functions with while loops
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nplease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}!")