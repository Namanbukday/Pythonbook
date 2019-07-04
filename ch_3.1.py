color = ['g', 'b', 'r', 'z', 'p', 'k']
print(color)

print("sorry to say, but 'g will not eb able to join our party.")
color.remove('g')
print("but 'c' will make it to the party")
color.insert(0, 'c')
print(color)

print("hey,since more people are joining us, so i found a bigger table for us!!")

print("\n at the begining:")
color.insert(0, 'qw')
print(color)

print("\n at the middle:")
color.insert(3, 'er')
print(color)

print("\n at the end:")
color.insert(-1, 'ty')
print(color)

print("only 2 guests can be invited:")
for i in color[2:]:
    print("sry cant invite you",color.pop())

print(color)
for i in color:
    print("welcome",i)

del color[0]
del color[1]
print(color)