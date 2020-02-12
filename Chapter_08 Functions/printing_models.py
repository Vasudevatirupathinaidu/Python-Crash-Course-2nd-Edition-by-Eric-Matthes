# Modifying a List in a Function

# Start with some designs that need to be printed.
def print_models(unprinted_designs, completed_models):
    """
    Simulate printed each design, until none are left.
    Move each design to complete_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs) # Empty list
# print("\n")

# Preventing a Function from Modifying a List by using slice. But It’s more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially when you’re working with large lists.
print("Preventing a Function from Modifying a List: ")
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)