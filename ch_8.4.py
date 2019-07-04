# PASSING AN ARBITRARY NUMBER OF ARGUMENTS

'''
def pizza(*toppings):
    print("adding: ")
    for i in toppings:
        print("\t-",i)


pizza('as')
pizza('as', 'df', 'gh')
'''

# mixing postional and arbitrary arguments
'''
def make_pizza(size, *toppings):
    print("\nyou ordered an " + str(size) + " inch pizza")
    for i in toppings:
        print("toppings are: ", i)


make_pizza(12, 'df', 'fdf', 'ee')
'''

# using arbitrary keyword arguments
'''
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for i, j in user_info.items():
        profile[i] = j
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
'''

