str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1])   #a

print(str[0:5])  # if you want substring in python

print(str+str1)   # concatenation

print(str3 in str)  # substring check, if you want check word in other string

var = str.split(".") # split the sentence using any letter or dots
print(var)
print(var[0]) # to print the values using index 0, 1
str4 = " great "
print(str4.strip()) # To remove space from string both side left & right
print(str4.lstrip()) # remove space in left

print(str4.rstrip()) # remove space in right