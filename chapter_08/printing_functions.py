"""functions related to 3d models."""
def printing_models(unprint_designs, completed_designs):
     """Simulate printing each design, until there are none left.Move each design to completed_models after printing."""
     while unprint_designs:
         current_design = unprint_designs.pop()
         print(f"printing model: {current_design}")
         completed_designs.append(current_design)
    
def show_completed_models(completed_designs):
    """show all the models that we are printed"""
    print("\nThe following models have been printed:")
    for completed_design in completed_designs:
        print(completed_design)
