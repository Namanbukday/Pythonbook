# JSON load() AND dump() :

# writing nos using dump() :

import json

numbers = [1, 2, 3, 4, 5]

f = 'numbers.json'  # its customary to write .json after the file name as an extension
with open(f, 'w') as f_obj:
    json.dump(numbers, f_obj)  # json.dump() always takes 2 arguments - a peice of data and the file object
