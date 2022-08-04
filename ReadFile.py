#syntax to open a txt file in python, if its in same project folder
file = open("Readfile.txt") # if you use this syntax , then you have to write the file.close()code, its mandatory

#another way of opening file, no need to write the file.close()code, it will close automatically
with open("Readfile.txt") as file: # by default its in read mode
    file.close()



with open("Readfile.txt","r") as file:  # Read mode
    file.close()



with open("Readfile.txt","w") as file:  # for write mode
    file.close()



#syntax to read all the content in the file
print(file.read())

#It will read the first 5 characters/bytes of the file
print(file.read(5))

#Syntax to read the complete line in the file, it will read the first line
print(file.readline())

#It will read the second line, as 1st line is already read by the above code
print(file.readline())

#syntax to close the file, very imp to do it
file.close()

#Print line by using the readline method

value = file.readline()

while value != "": # value not equal to blank that means value is present , loop will run , if not loop will stop
    print(value)
    value = file.readline()

file.close()

#Readlines methods

#It will print like a list (['Devashish\n', 'subhashree\n', 'Daddy\n', 'Mummy\n', 'Auncle\n', 'Aunty']
print(file.readlines())

#Print lines using readlines methods, very imp & useful for framework

value = file.readlines()
for a in value: # ran for loop to extract the values from the list
    print(a)

file.close()

