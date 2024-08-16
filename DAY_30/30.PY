# 🍵 , Hanji Kaise ho aap sabhi this is 29th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

"""

Improve the password manager.

"""

# ------------------------ Handling Errors & Exceptions ----------------------- #

# with open("a_file.txt") as file:
# file.read()

#  KeyError
# a_dict={"key":"value"}
# value = a_dict["non_existent_key"]

# IndexError
# fruits=["Apple","Banana","Pear"]
# fruit=fruits[3]

# TypeError
# text="abc"
# print(text+5)

# Handling Exception
# try: 
#     Something that might cause an exception

# except:
#     Do this if there was an exception

# else:
#     Do htis if there were no exceptions

# finally:
#     Do this no matter what happens

# Always finally block is executed

# FileNotFound
try:
    file=open("a_file.txt",mode="r")
    a_dict={"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    # print("There was an error.")
    file=open("a_file.txt","w")
    file.write("somethinng")
except KeyError as error_message:
    print(f"The key {error_message} does not exsits")
else:
    # if no exception then this block is executed
    content=file.read()
    print(content)
finally:
    print("File was closed.")     
    raise KeyError
    raise   TypeError("This is an typerror")

# ---------------------------- OWN EXCEPTION ------------------------------- #

height = float(input("heights: "))
weight = float(input("weights: "))

if height>3:
    raise ValueError("Human height ahould not be over 3 meters.")

bmi = weight/height**2
print(bmi)

"""Add data i json file"""
    
    
