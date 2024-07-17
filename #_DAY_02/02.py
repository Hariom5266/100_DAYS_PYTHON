# 🍵 , Hanji Kaise ho aap sabhi this is 2nd day of #100Days_Of_Python

# ============================ DATATYPES ================================ #

# ! print(len(12345)) #it give error

# 1> string
# 2> int
# 3> flaot 
# 4> boolean

#string :
print("Hello"[4])

#Integer :
print(123+345);

# TODO : 123_456_678 = 123456789 #both are same

#Float :
# 3.14159

#Boolean :
# True
# False

#Quiz :
street_name = "abbey Road"
print(street_name[4] + street_name[7])

# Function : machine like potato to chips converter

num_char = len(input("what is your name : "))
# ! print("Your name has " + num_char + " Character.") # we cant do like this print len of str

# num_char = str(len(input("what is your name : ")))
# print("Your name has " + num_char + " Character.") # we can do like this print len of str

print(70 + float(100.5))

print(str(70) + str(100))

#Coding Challenge

two_digit_number = input()
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
sum = first_digit + second_digit
print(sum)

# 3 + 5
# 7 - 3
# 3 * 2
# 10 / 5
#2 ** 3 = 8

# print(type(6/3))
print(2 ** 10)

# ====== Multi line Comments ====== #

""" 
python follow : 
PEMDASLR

Parentheses -- ()
Exponents -- **
Multi -- * 
Divi -- /
Add -- +
Subtract  --> -

Importance :
() , ** , * / , + - 
Calculation doing left to right order
3*3+3/3-3
----------> order
"""

print(3*3+3/3-3)
print(3 * (3 + 3)/3 - 3)

#BMI CALC

# round the numbers
print(round(8/3))
print(round(8/3 ,2))
print(8 // 3) # it say float division and convert in int
print(type(8 // 3))

score = 0
height = 1.5
isWinning = True;

#f-string
print(f"your score is {score}, height is {height} and your result is {isWinning}")













