# EXCEPTIONS :

# Handling a zeroDivisionError exception :
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("you cant divide by zero!!!")
'''

# Using exceptions to prevent crashes :
# building a simple calculator :
'''
print("give me 2 nos and i'll divide them for you")
print("enter 'q' to quit\n")

while True:
    f = input("enter no. 1:")
    if f == 'q':
        break
    s = input("enter no. 2:")
    if s == 'q':
        break
    try:
        ans = int(f)/int(s)
    except ZeroDivisionError:
        print("you cant divide by zero!!!")
    else:
        print(ans)
'''

# Handling FileNotFoundError Exceptions :
'''
f = 'alice.txt'

try:
    with open(f) as f_obj:
        contents = f_obj.read()
        print(contents)
except FileNotFoundError:
    print("file not found")
'''

# Analyzing texts : WE WILL BE USING SPLIT() FUNCTION TO COUNT THE WORDS
# THEN STORE THEM IN A LIST AND USING ITS LENGTH TO PRINT HOW MANY WORDS ARE THERE

'''
f = 'texts.txt'

try:
    with open(f) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("file"+ f + "not found")
else:
    # count the approximate number of words
    words = contents.split()
    t_words = len(words)
    print(t_words)
'''

# Working with multiple files :
# WE WILL PUT ABOVE EXAMPLE IN A FUNCTION THAT WILL MAKE IT EASIER TO UNDERSTAND THE CODE BETTER

'''
def count_words(f):
    try:
        with open(f) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("file :" + f + ": not found")
    else:
        # count the approximate number of words
        words = contents.split()
        t_words = len(words)
        print(t_words)


f = ['alice.txt', 'texts.txt', 'ko.txt']
for i in f:
    count_words(i)
'''

# Using pass statement :

'''
try:
    .
    .
    .
except FileNotFoundError:
    pass
else:
    .
    .
    .
'''

'''
while True:
    print("\nenter 2 nos and i'll add them")
    print("enter 'q' to quit")
    try:
        f = input("first no:")
        if f == 'q':
            break
        s = input("second no:")
        if s == 'q':
            break
        ans = int(f) + int(s)
    except ValueError:
        print("\nyou have to enter a number!!")

    else:
        print(ans)
'''


def print_contents(f):
    try:
        with open(f) as f_obj:
            contents = f_obj.read()
            print(contents,"\n")
    except FileNotFoundError:
        print("file isnt there")


f = ['cats.txt', 'dogs.txt']
for i in f:
    print_contents(i)
