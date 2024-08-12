# 🍵 , Hanji Kaise ho aap sabhi this is 26th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ==================== LIST COMPREHENSION ==================== #

# Make list from previous list called list comprehension, Also can work with string and or sequncese

# new_list=[new item fro item in list]

numbers=[1,2,3,4,5]
new_list=[n+1 for n in numbers]
print(new_list)

name="Hariom"
new_name=[c for c in name]
print(new_name)

range_list=[new_item*2 for new_item in range(1,5)]
print(range_list)

# Conditional list comprehension

# new_list=[new item in list if test]

nums=[1,2,3,4,5,6,8,10,13]
new_nums=[num for num in nums if num%2==0]
print(new_nums)

#  Ctrl + c for stop infinite loop
# i=0
# while(True):
#     print(i)
#     i+=1

names=["Hari","Hariom","Harish","Hiren","HC_Joshi","Chetan"]

long_names=[name.upper() for name in names if len(name)>5]
print(long_names)








