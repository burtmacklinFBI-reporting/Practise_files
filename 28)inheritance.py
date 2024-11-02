class Vehicle:
    def general_usage(self):
        print('general usage: transportation')

class Car(Vehicle): # this is called inheritance and now it will be having all the properties of the above class
    def __init__(self):
        print(''' I'm a car''')
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")

class Motorbike(Vehicle): # this is called inheritance and now it will be having all the properties of the above class
    def __init__(self):
        print(''' I'm a bike''')
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing")
        
c = Car()
(c.specific_usage())

print(issubclass(Car,Vehicle)) # built in function in subclass where you can check whether a subclass is really a subclass.



class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")


class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel") #super is a built in way for us to acces the properties of the super class and to acess its methods.

    def sound(self):
        print("Woof woof!")


x = Dog()
x.print_habitat()
x.sound()