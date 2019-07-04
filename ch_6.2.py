#LOOPING through a dictionary:

#looping through key- value pairs;items():
'''
user = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

# we use items() func and 'keys' 'names' are the variable used to traverse through the dicitonary
for keys,names in user.items():
    print("\nkeys are : ",keys)
    print("names are : ",names)
'''

#looping through all "keys" in the dictionary;keys():
'''
lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for i in lang.keys():
    print("names are ",i.title())
'''

#looping through a dictionary's 'keys'in order;sorted(keys()):
'''
lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for  i in sorted(lang.keys()):
    print("names in alphabetical order :",i.title())
'''

#loopin through all "values" in a dictionary;values():
'''
lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for i in lang.values():
    print("their favorite languages are :",i.title())
'''

#if you have to exclude the  repeated values,use set() func:
'''
lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for i in set(lang.values()):
    print("favorite languages are :",i.title())
'''

alien = {}
alien['color0'] = 'green'
alien['points0'] = 5
alien['color2'] = 'blue'
alien['points2'] = 10
alien['color3'] = 'voilet'
alien['points3'] = 25
alien['color4'] = 'olive'
alien['points4'] = 50
alien['color5'] = 'grey'
alien['points5'] = 100
print(alien)

for i,j in alien.items():
    print(i)
    print(j)