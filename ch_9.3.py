# ..................INHERITANCE.................
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
        print("\nthis car has ", self.odometer, "on odometer.")

    def increment_odometer(self, miles):
        self.odometer += miles
        # return self.odometer

    def fill_gas_tank(self):
        print("filling up the gas tank")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    #def describe_battery(self):
       # print("battery size is :", self.battery_size)

    def fill_gas_tank(self):
        print("no need for gas coz its a tesla,son")


class Battery():

    def __init(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("the car has" + str(self.battery_size) + " KWhbattery left in it")


my_tesla = ElectricCar('tesla', 'model-s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

my_tesla.fill_gas_tank()

m = Car('audi', 'a6', 2018)
m.fill_gas_tank()

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




class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavours = ['vanila' ,'chocolate', 'strawberry', 'butterscotch', 'mint_chocolate']

    def show_flavours(self):
        print("there are",len(self.flavours),"flavours")
        print("which are:")
        for i in self.flavours:
            print("\t-",i)


icecream = IceCreamStand('mc donalds', 'american')
icecream.show_flavours()

'''

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


class Admin(Users):

    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privileges = ["can add a post", "can delete a post", "can modify a post", "can destroy the whole file"]


class Priviliges():

    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("the admin has the following privileges: ")
        for i in self.privileges:
            print("\t -", i)


ad = Admin('naman', 'bukday')
# ad.show_privileges()

p = Priviliges("can add a post", "can delete a post", "can modify a post", "can destroy the whole file")
p.show_privileges()

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
        print("\nthis car has ", self.odometer, "on odometer.")

    def increment_odometer(self, miles):
        self.odometer += miles
        # return self.odometer

    def fill_gas_tank(self):
        print("filling up the gas tank")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    # def describe_battery(self):
    # print("battery size is :", self.battery_size)

    def fill_gas_tank(self):
        print("no need for gas coz its a tesla,son")


class Battery():

    def __init(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("the car has" + str(self.battery_size) + " KWhbattery left in it")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            r = 240
        elif self.battery_size == 85:
            r = 270

        message = "This car can go approximately " + str(r)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size <= 85:
            self.battery_size = 85


my_tesla = ElectricCar('tesla', 'model S', 2019)
my_tesla.battery.get_range()
#b = Battery()
