# Python Tuple Data Type
# it is same like array but it allows multiple values & can be of different types (Int, float , str etc)
# https://www.journaldev.com/14036/python-data-types
# Tuple is immutable - Means you cannot update the value once its declared, refer last line of code
# small Syntax change in tuple () instead of [] , while declaring the variable

values = (1, 2, "Devashish", 4, "Mumbai")
print(values[0]) # start with O index , same like array
print(values[1])
print(values[2])
print(values[3])
print(values[4])
print(values) # print the complete values

print(values[-1]) # to print the last value within the list
print(values[1:3]) # it will print the index value of 1 & 2
print(values)

# values.insert(3, 'Nath') # Insert the new index value
# values.append("End") # Adding the new values in the last index
# values[2] = "DEVASHISH" # Updating the existing the value, mutable




