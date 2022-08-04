# 3 types of exception
# raise
# assert
# try , except (catch)

Itemscart = 0
# scenario - 2 items will be added into the cart

# if Itemscart != 2:
# raise Exception("Products cart count not matching") # Exception to throw error, if failed

assert (Itemscart == 2)  # Assert will work, if only true , if condition - false then it will throw exception
