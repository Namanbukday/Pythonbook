# USING load() FUNCTION TO READ NOS FROM THE MEMORY :

import json

f = 'numbers.json'

with open(f) as f_obj:
    numbers = json.load(f_obj)  # we use json.load() to load the info from 'numbers.json' to a variable 'numbers'
    print(numbers)
