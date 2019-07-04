# functions
'''
def greet_user(user):
    print("hello, "+ user)

greet_user('naman')
'''

# passing arguments:

# 1. positional arguments:
'''
def pet(name, age):
    print("\nname is ", name)
    print("and its age is ", age)


pet('willie', 6)
pet('max', 2)
'''


# 2. keyword arguments:
'''def pet(name, age):
    print("\nname:", name)
    print("age:", age)


pet(name='maxy', age=6)
'''


# 3. default values:
'''def pet(name, age=6):
    print("name", name)
    print("age", age)


pet('willie')'''


# equivalent function calls:
'''
def pet(name, age = 6):
    print("\nname is ", name)
    print("and its age is ", age)


pet('willie')
pet(name = 'willie')
pet('h', 8)
pet(age = 12, name ='fu')
'''


#1
def make_shirt(size='L', mess='i love python'):
    print("\nshirt size is:", size)
    print("and the message to be printed on the shirt is:",mess)


make_shirt('L')
make_shirt('M')
make_shirt('S', 'scooby dooby')


#2
def describe_city(city, country='Switzerland'):
    print("\n"+city.title()+" is in "+country.title())


describe_city('adsf')
describe_city('dsee')
describe_city('fvvx')