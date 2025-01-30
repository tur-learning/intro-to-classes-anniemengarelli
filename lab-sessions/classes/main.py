from classes import Person

person1 = Person("Annie", 21, 175)
person1.info()
person1.change_age(22)
person1.info()

person2 = Person("Alex", 22, 175)
person2.info()

from classes import Pizza # this is importing the class I made in the other file

pizza1 = Pizza("tomato", "mozzarella", 7) # this is providing the data and establishing it as a pizza (something that fits in the class)
pizza1.info() # this is printing the data
pizza1.change_topping1("basil") # this is changing the first topping
pizza1.change_size(7) # this is converting the size of the pizza from inches to centimeters

pizza2 = Pizza("onion", "chicken", 8)
pizza2.info()
pizza2.change_topping1("spinach")
pizza2.change_size(8)

pizza3 = Pizza("prosciutto", "arugula", 4)
pizza3.info()
pizza3.change_topping1("peppers")
pizza3.change_size(4)