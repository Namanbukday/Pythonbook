# MORE WORKING WITH CLASSES AND INSTANCES

'''
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 100

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("\nyou can't roll back odometer!!")

    def read_odometer(self):
        print("\nthis car has ",self.odometer, "on odometer.")

    def increment_odometer(self, miles):
        self.odometer += miles
        # return self.odometer

my_new_car = Car('audi', 'a6', 2017)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(4000)
my_new_car.read_odometer()

my_new_car.increment_odometer(2100)
my_new_car.read_odometer()
'''

'''
class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print("\nWelcome to " + self.name.title() + ",")
        print("its an " + self.cuisine.title() + " cuisine restaurant.")

    def open_restaurant(self):
        print("Restaurant is now open to public for the first time!!!")

    def set_number_served(self, v):
        self.number_served = v
        return self.number_served

    def increment_number_served(self, n):
        self.number_served += n
        return self.number_served


rest = Restaurant("alessamdro's", "italian")
rest.describe_restaurant()
rest.open_restaurant()

print("the number of customers served :", rest.number_served)
rest.number_served = 15
print("the number of customers served :", rest.number_served)
print(rest.set_number_served(11))
print("No. of customers served during a day are :", rest.increment_number_served(22))
'''


class Users():

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + " " + self.l_name
        self.login_attempts = 0

    def describe_user(self):
        print("user name is: " + self.f_name + " " + self.l_name)

    def greet_user(self):
        print("what's up, ", self.full_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0


u = Users('naman', 'bukday')
u.describe_user()
u.greet_user()
for i in range(1, 11):
    u.increment_login_attempts()

print("login attempts = ", u.login_attempts)

u.reset_login_attempts()
print(u.login_attempts)
