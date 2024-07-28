# 🍵 , Hanji Kaise ho aap sabhi this is 13th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# =================== Debugging =================== #

# Grace hopper lady who find debugging 

#  How to debug code
# 1. Describe the problem
def my_function():
    for i in range(1,20): # -- think here range fnc got at 1 to 19 so not anything print here so do here 21 at 20
        if i==20:
            print("You got it.")
my_function()            

# =================== Reproduce the bug =================== #

from random import randint
dice_imgs = ["0","0","0","0","0","0"]
dice_num = randint(1,6) # do here 0 to 5 number
print(dice_imgs[dice_num])

# =================== Play Computer =================== #
year=int(input("What's your year of birth?\n"))
if year>1980 and year<1994:
    print("You are a millenial.")
elif year>=1994:
    print("You are a Gen Z.")

# =================== Fix the Errors --  watching red underlines =================== #

age = input("How old are you?\n") # do here int 
if age>18:
# print(f"You can drive at age {age}.") -- it throw indentation error
    print(f"You can drive at age {age}.")


# =================== Print is your friend -- Squash bugs with a print() =================== #

pages = 0
word_per_page=0
pages=int(input("Number of pages: "))
word_per_page=int(input("Number of words per pages: ")) # becuse here == 
total_words=pages+word_per_page
print(f"Pages: {pages}, word_per_page: {word_per_page}")
print(total_words)


# =================== Bring out the BIG Gun: Using a Debugger =================== #

# Thony or pythontuttor

def mutate(a_list):
    b_list=[]
    for item in a_list:
        new_item = item*2
        b_list.append(new_item)
    # b_list.append(new_item) -- not write like it like write above
    print(b_list)

mutate([1,2,3,5,8,13])

# =================== Final Debugging Tips =================== #

# Take a Break
# Ask a Friend
# Run Often
# Ask Stackoverflow

# Everyone gets bugs.
