# modifying a list in a function

#start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#simulate printing each design, until none are left.
#move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"printing model: {current_design}")
    completed_models.append(current_design)

#display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#modify list with functions
print('\n----with functions-----')
def print_models(unprinted_designs, completed_models):
    """
    simulate printing each design, until none are left.
    move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """show all models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

#preventing a function from modyfying a list
# The slice notation [:] makes a copy of the list to send to the function.
# If we didn’t want to empty the list of unprinted designs
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
