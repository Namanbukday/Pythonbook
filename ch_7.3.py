# using while loop with list and dictionary:
# moving items from one list to another:
'''
u = ['as', 'df', 'gh']
q = []
while u:  # until all the users are there in U
    w = u.pop()
    q.append(w)

print(q)
'''

# removing all instances (repetitive values) of specific values from a list:
'''
p = ['a', 'c', 's', 'd', 'c', 'f', 'g']
print(p)

while 'c' in p:
    p.remove('c')
    
print(p)
'''

# filling a dictionary with user input:
'''
l= {}

flag = True

while flag:
    name = input("\nenter name")
    ln = input("enter last name")

    l[name] = ln   # adding name and last name as keys and values one by one
    repeat = input("\nwant to continue:yes /no")
    if repeat == "yes":
        continue
    else:
        print(l)
        flag = False
'''

sandwich_orders = ['tu', 'pa', 'ch', 'pa', 'mc']
finished_sandwich = []

while sandwich_orders:
    f = sandwich_orders.pop()
    if f == 'pa':
        sandwich_orders.remove('pa')
    else:
        print("finished "+ f +" sandwich")
        finished_sandwich.append(f)

print(sandwich_orders)
print(finished_sandwich)
