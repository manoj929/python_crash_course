# positional arguments
# make sure the order of the
# arguments in your function call matches the order of the parameters
def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have {animal_type}")
    print(f"my {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
#multiple function call
describe_pet('dog', 'rockie')

#keyword arguments
# When you use keyword arguments, be sure to use the exact names of the parameters in
# the function’s definition
def about_animal(pet_type, pet_name):
    print(f"\nI have a {pet_type}")
    print(f"my{pet_type}'s name is {pet_name}.")

about_animal(pet_name = 'sultan', pet_type = 'dog')
#the order of keyword argument doesn't matter
about_animal(pet_type = 'cat', pet_name = 'brook')

#default values
def pet_animal(pet_name, pet_type = 'dog'):
    print(f"\nI have a {pet_type}")
    print(f"my{pet_type}'s name is {pet_name}.")

pet_animal('james')

#equivalent function calls
pet_animal('willie')
pet_animal(pet_name = 'maggi', pet_type = 'cat')
pet_animal('julie', 'dog')

#avoiding arument errors
# pet_animal()
# pet_animal('ruby', 'cat', 12)