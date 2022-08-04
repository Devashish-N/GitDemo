# Class in python consists of (Variables, Methods, constructor)

class firstclass():
    a = 20 # Variable created in Class

    def sum(self): # Method created in class , known as functions, if created independently
        print("Creating a first method")


obj = firstclass() # calling of a class by creating object
obj.sum() # Calling of method within a class
print(obj.a) # calling of variable within a class
