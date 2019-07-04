# PASSING A LIST

'''
def greet_users(names):
    for i in names:
        print("hello, " + i)


username = ['as', 'as', 'sd']
greet_users(username)
#greet_users(['as', 'sd', 'tr'])
'''

# modifying a list in a function
'''
def m(u_model, c_model):
    while u_model:
        c = u_model.pop()
        print("making", c)
        c_model.append(c)


def show(c_model):
    for i in c_model:
        print("items in  new list are:"+ i)


uu = ['as', 'ad', 'fg']
cc = []
m(uu, cc)
show(cc)
'''


# preventing a function to modify a list
# you can do this by sending a copy of the list
# syntax = function_name(list_name[:])


def magicians(names):
    for i in names:
        print(i)


def make_great(names):
    while names:
        x = names.pop()
        x = "the great " + x
        n.append(x)
    print(n)


def show(n):
    for i in n:
        print(i)


name = ['as', 'df', 'fg']
n = []
magicians(name)
make_great(name[:])
show(n)