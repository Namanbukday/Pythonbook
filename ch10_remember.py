import json

f = 'usernam.json'
try:
    with open(f) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what is your name ?")
    with open(f, 'w') as f_obj:
        json.dump(username, f_obj)
        print("we'll remember you cunt")
else:
    print("welcome back " + username + "!")
