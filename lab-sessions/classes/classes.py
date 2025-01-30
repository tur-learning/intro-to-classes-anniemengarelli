# First creating a class
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def info(self):
        print(self.name, self.age, self.height)

    def change_age(self, new_age):
        self.age = new_age


class Pizza:
    def __init__(self, topping1, topping2, size): # Here I am defining the elements necessary for something to qualify as Pizza
        self.topping1 = topping1
        self.topping2 = topping2
        self.size = size

    def info(self): # Here I am defining what the program will be displaying 
        print(self.topping1, self.topping2, self.size)

    def change_topping1(self, new_topping1): # Here I am adding in a method to change a topping
        self.topping1 = new_topping1
    
    def change_size(self, centimeters): # Here I am converting the inches to cm
        centimeters = int(self.size)*2.54
        print(self.topping1, self.topping2, centimeters)

