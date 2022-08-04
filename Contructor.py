# Contructor name should be __init__ (not the class name like in java)
# new keyword is not required when you create object
# self keyword is mandatory, if you call variable name into a method
# Class variable & instance variable have whole different purposes
# Self parameter comes default in any method in the class


class Calculator:
    num = 100  # Class variable

    # this is the constructor
    def __init__(self, a, b):
        self.firstnumber = a  # Calling an instance variable , self keyword is mandatory
        self.secondnumber = b

    def getdata(self):
        print("Executing a new method in a class")

    def summation(self):
        return self.firstnumber + self.secondnumber + self.num  # Can also use Classname keyword


obj = Calculator(5, 5)
obj.getdata()
print(obj.summation())

obj1 = Calculator(6, 6)
obj1.getdata()
print(obj1.summation())
