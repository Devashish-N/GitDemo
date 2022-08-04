# Inheritance, you can inherit all the methods & functions from the parent class
from Contructor import Calculator


class ChildImpl(Calculator):
    num2 = 200  # Class variable

    # this is the constructor
    # always check, if the parent class has a constructor defined along with same code,
    # If not, then by default constructor will run automatically
    # If yes, then please call the parent constructor from child constructor, its imp , line 12 & 13
    def __init__(self): # child class constructor
        Calculator.__init__(self, 10, 20) # called the parent class constructor

    def getcompletedata(self):
        return self.num + self.num2 + self.summation()


obj = ChildImpl()
print(obj.getcompletedata())
