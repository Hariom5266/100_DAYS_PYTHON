# 🍵 , Hanji Kaise ho aap sabhi this is 4th day of #100Days_Of_Python I'm back and ready to code.

# =========================== Randmisation and lists ================================ #
# pseudo random generator -- referance of khan acedemy for more on it
#askpython.org -- for any query in python

import random
import my_modul
random_integer = random.randint(1,10)
print(random_integer)

# what is module?
# split the code in chunk where each chunk is resposinle for a different bit of funcnality of your program. It chunk known as a module.

print(my_modul.pi)

# Create random float number
random_float = random.random()
print(random_float) # range 0.000000000... --- 0.999999999999999..
print(random_float*5) #then it generate float number between 1 to 5

# ================================ Updated Versionof love calculator ======================== #
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")




