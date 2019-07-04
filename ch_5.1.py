# using IF with lists
'''
l  = ['mu', 'df', 'gh']

for i in l:
    if i == 'mu':
        print("out of order")
    else:
        print("adding: "+i)
'''

# checking if the list is empty or not:
'''l = []
if l:
    ......
else:
    print("empty list!!!")
'''

# using multiple lists
'''
l  = ['mu',"kl", 'df', 'gh']
a  = ['mu', 'aa']

for i in a:
    if i in l:
        print("same")
    else:
        print("oho")
'''

user_names = ["admin", "qw", "er", "ty", "yu", "io"]

if user_names:
    for i in  user_names:
        if i == "admin":
            print("hello there....admin")
        else:
            print("hello,"+i.title())
else:
    print("list is empty!!")

l = list(range(1,10))
print(l)
for i in l:
    if i == 1:
        print(str(i)+"st")
    if i == 2:
        print(str(i)+"nd")
    if i == 3:
        print(str(i)+"rd")
    if i > 3:
        print(str(i)+"th")