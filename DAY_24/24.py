# 🍵 , Hanji Kaise ho aap sabhi this is 24th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ===================== CRUD OPERATION WITH FILES ===================== #

# Mode of open the files:
# mode="r"
# mode="w"  ---> Replace the file content , cretae file if not exists
# mode ="a" ----> Apped the file content

# Reading file

file = open("C:/Users/Lenovo/Desktop/01_HC_JOSHI/Work/100_DAYS_OF_PYTHON/DAY_24/my_file.txt",mode='a')
# contents = file.read()
# print(contents)

# Write in file

file.write("\nNew Text.")

file.close()


# Deferent Way to open the file

# with open("C:/Users/Lenovo/Desktop/01_HC_JOSHI/Work/100_DAYS_OF_PYTHON/DAY_24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
