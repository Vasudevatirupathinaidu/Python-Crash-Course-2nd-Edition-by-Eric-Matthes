# Modifying a List in a Function
import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs) # Empty list
# print("\n")

# Preventing a Function from Modifying a List by using slice. But It’s more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially when you’re working with large lists.
print("Preventing a Function from Modifying a List: ")
pf.print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)
print(unprinted_designs)