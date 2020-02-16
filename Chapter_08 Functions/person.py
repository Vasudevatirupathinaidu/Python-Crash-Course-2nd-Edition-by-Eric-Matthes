# Returning a Dictionary

import person_functions

musician = person_functions.bulid_person('Vasudev', 'Bonu', age = 27)
print(musician)
print("\n")


import person_functions as pf

musician = pf.bulid_person('Vasudev', 'Bonu', age = 27)
print(musician)
print("\n")


from person_functions import bulid_person

musician = bulid_person('Vasudev', 'Bonu', age = 27)
print(musician)
print("\n")


from person_functions import bulid_person as bp

musician = bp('Vasudev', 'Bonu', age = 27)
print(musician)
print("\n")


from person_functions import *

musician = bulid_person('Vasudev', 'Bonu', age = 27)
print(musician)
print("\n")