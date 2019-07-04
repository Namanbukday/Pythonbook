# CLASSES
'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("your dog's age is : ", self.age)

    def sit(self):
        print(self.name.title() + " is sitting.")

    def rolled_over(self):
        print(self.name.title() + " just rolled_over")



m = Dog('ad', 5)
m.sit()
m.rolled_over()
'''

'''
class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print("\nWelcome to " + self.name.title() + ",")
        print("its an " + self.cuisine.title() + " cuisine restaurant.")

    def open_restaurant(self):
        print("Restaurant is now open to public for the first time!!!")


rest = Restaurant("alessamdro's", "italian")
rest.describe_restaurant()
rest.open_restaurant()
'''


class Users():

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + " " + self.l_name

    def describe_user(self):
        print("user name is: " + self.f_name + " " + self.l_name)

    def greet_user(self):
        print("what's up, ", self.full_name.title())


u = Users('naman', 'bukday')
u.describe_user()
u.greet_user()
