import json

f = 'username.json'

with open(f) as f_obj:
    username = json.load(f_obj)
    print("hello " + username + ", see we remember your punkass.")
