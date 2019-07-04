# WRITING TO A FILE :

# Writing to an empty file:

# f = 'ch10_1.txt'

# with open(f, 'w') as f_obj:
# f_obj.write("I love programming!")
# f_obj.write('wazzzuppp') # writing multiple lines

# Appending to a file :

# f = 'ch10_1.txt'

# with open(f, 'a') as f_obj:
# f_obj.write("let me check")


# p = input("please enter your name:")

fa = 'guest.txt'
p = ''
q = ''
with open(fa, 'w') as f_obj:
    while True:
        p = input("please enter your name:")
        if p == 'q':
            break
        f_obj.write("\n" + p + "\n")
        print("wazzzuup " + p + " and thank you for staying here.")
        f_obj.write("wazzzuup " + p + " and thank you for staying here.\n")
        q = input("how was your stay in our hotel?")
        if q == 'q':
            break
        f_obj.write("how was your stay in our hotel?")
        f_obj.write(q + "\n")
