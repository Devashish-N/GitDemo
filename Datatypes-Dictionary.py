# Python Dictionary Data Type
# https://www.journaldev.com/14036/python-data-types
# Dictionaries are written within curly braces in the form key:value.
# No matter key or values, if its string then it should be in double quotes "", syntax {} bracket

a = {1: "Devashish", "Name": "last name", "age": 33}

print(a) # Print the complete values

print(a[1])
print(a["age"])
print(a["Name"])

# How to dynamically create dictionary on runtime

dict = {}  # Dictionary is empty now
# Now will add key:value on runtime & print it

dict["First Name"] = "Devashish"
dict["Last Name"] = "Nath"
dict[20] = "Age"

print(dict)

# Print the value as per the key

print(dict["First Name"])
print(dict["Last Name"])
print(dict[20])
