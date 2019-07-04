# introducing WHILE loop:
'''
count = 1
while count <= 5:
    print("#" * count)
    count += 1

print(count)
'''

# letting user when to quit:
'''
prompt = ("\n enter anthying")
prompt += ("to quit the loop, enter 'quit'.")

message = " "

while message != "quit":
    if message != "quit":
        message = input(prompt)

    else:
        print(message)
'''

# using a flag:
'''
prompt = "\n enter anthying"
prompt += " to quit the loop, enter 'quit'."

flag = True
message = " "

while flag:
    message = input(prompt)
    if message != "quit":
        print(message)
    else:
        flag = False
'''

# using BREAK in a loop:
'''
prompt = "\n enter anthying"
prompt += " to quit the loop, enter 'quit'."

while True:
    message = input(prompt)
    if message != "quit":
        print(message)
    else:
        break
'''

# using continue:
'''
c = 0

while c <= 11:
    c += 1
    if c % 2 == 0:
        print(c)
'''

p = "\n Enter your age"
p += "\n And enter 'quit' to quit"
m = " "
while m != "quit":
    m = int(input(p))
    if m < 3:
        print("free")
    if m < 12:
        print("$10")
    if m > 12:
        print("$15")
    if m == "quit":
        break

