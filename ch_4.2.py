# making numerical list:
'''
m = []

for i in range(0,6):
    m.append(i)

print(m)
'''

'''
#using list()
m = list(range(0,6))
print(m)
'''

'''
# for even numbers
even_nos = list(range(0,21,2))
print(even_nos)
'''

'''
# for square numbers
sq = []
for i in range(0, 10):
    sq.append(i ** 2)

print(sq)
'''

'''
# list comprehension
square = [i ** 2 for i in range(0, 10)]
print(square)
'''

l = list(range(1,21))
print(l)

print(min(l))
print(max(l))
print(sum(l))

print("list of first 10 cubes")
m = [i ** 3 for i in range(1,11)]
print(m)