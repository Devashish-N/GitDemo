# Read the file & store in the list
# Reversed the list
# write the list into the file

with open("Readfile.txt", "r") as reader:  # Open the file & read it
    file = reader.readlines()  # Capture the values in a list using a variables file
    reversed(file) # syntax to reverse the content
    with open("Readfile.txt", "w") as writer:  # open the file & write it
        for content in reversed(file):  # for loop to extract the value from list
            writer.write(content)  # write the extracted value in the file
