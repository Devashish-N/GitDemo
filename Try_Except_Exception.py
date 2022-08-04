# If you have scenario, where you are not sure about the condition -it might pass or fail
# then except block will help to continue the TC ,


try:
    with open("Readfiles.txt", "r") as file:  # File does not exist- except block, if exist- dont go to except block
        file.read()

except:
    print("exception in try block, TC will be continue")  # printing the message , provided by us

###########################################################################################################

try:
    with open("Readfiles.txt", "r") as file:  # File does not exist, went to except block
        file.read()

except Exception as e:  # syntax to get the exact error from the try block
    print(e)  # printing the exact error generated in the try block

###########################################################################################################
# finally keyword , will execute in all scenario's (pass & fail)
# Example - Test executed, you want to delete cookies, clear data, its helpful


try:
    with open("Readfiles.txt", "r") as file:  # File does not exist, went to except block
        file.read()
except Exception as e:  # syntax to get the exact error from the try block
    print(e)
finally:
    print("Delete cookies, clear the test data, close the browser")
