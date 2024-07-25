#🍵, Hanji Kaise ho aap sabhi this is 3rd day of #100Days_Of_Python

# =========================== Nested If-Else ================================== #

# print("Welcom to the rollercoaster!")
# height = int(input("What is your height in cm?"))

# if height>=120:
#     print("You can ride the rollarcoaster!")
#     age = int(input("What is your age?"))
#     if age<12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
     
# else:
#     print("Sorry, you have to grow taller before you can ride.")
    
# =========================== BMI Advance Version ================================== #

# height_BMI = float(input("What is your height?"))
# weight_BMI = float(input("What is your Weight?"))
# BMI = weight_BMI/(height_BMI**2)

# if BMI < 18.51:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI < 30:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, you are obsese.")

# =========================== Leap Year Calculator ================================== #

# year = int(input("Enter Any year : "))

# if year % 4 == 0 :
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is leap year.")
#         else:
#             print(f"{year} not leap year.")
#     else:
#         print(f"{year} is leap year.")
# else:
#     print(f"{year} not leap year.")

# =========================== Multiple Condition ================================== #

# if condition 1:
#     DO A
# if condition 2:
#     DO B
# if condition 3:
#     DO C
    
# height = int(input("What is your Height?\n"))
# bill = 0
# if height >= 120:
#     print("You can ride the rollarcoaster!")
#     age = int(input("What is your age?\n"))
#     wants_photo = input("Do you want take a photo? Y or N.\n")
#     if age<12:
#         print("Child tickets are $5.")
#         bill+=5
#     elif age<=18:
#         print("Youth tickets are $9.")
#         bill+=9
#     else:
#         print("Adult tickets are $12.")
#         bill+=12
#     if wants_photo == "Y" or wants_photo == "y":
#         bill+=3
#         print(f"Your total tickets is ${bill}")
#     elif wants_photo == "N" or wants_photo == "n":
#         print(f"Your total tickets is ${bill}")
#     else:
#         print("Invalid Choice! Please Enter Valid choice.")
# else:
#     print("You can't ride rollarcoaster, before ride get long height!")

# =============================== LOGICAL OPERATOR =============================== #

# and
# or
# not

    
# height = int(input("What is your Height?\n"))
# bill = 0
# if height >= 120:
#     print("You can ride the rollarcoaster!")
#     age = int(input("What is your age?\n"))
#     wants_photo = input("Do you want take a photo? Y or N.\n")
#     if age<12:
#         print("Child tickets are $5.")
#         bill+=5
#     elif age>=45 and age<=65:
#         bill = 0
#         print(f"Your total tickets is ${bill}")
#         exit()
#     elif age<=18:
#         print("Youth tickets are $9.")
#         bill+=9
#     else:
#         print("Adult tickets are $12.")
#         bill+=12
#     if wants_photo == "Y" or wants_photo == "y":
#         bill+=3
#         print(f"Your total tickets is ${bill}")
#     elif wants_photo == "N" or wants_photo == "n":
#         print(f"Your total tickets is ${bill}")
#     else:
#         print("Invalid Choice! Please Enter Valid choice.")
# else:
#     print("You can't ride rollarcoaster, before ride get long height!")

# =============================== LOVE CALCULATOR =============================== #

print("The love calculator is calculating your score...!")
name1 = input("What is your name? ")
name2 = input("What is your partner name? ")

combined_names = name1+name2

lover_names = combined_names.lower()
t = lover_names.count("t")
r = lover_names.count("r")
u = lover_names.count("u")
e = lover_names.count("e")

l = lover_names.count("l")
o = lover_names.count("o")
v = lover_names.count("v")
e = lover_names.count("e")

first_digit = t+r+u+e
second_digit = l+o+v+e

score = int(first_digit+second_digit)

if score>10 and score<90:
    print(f"your score is : {score}, you go together like coke and mentos")
elif score>=40 and score<=50:
    print(f"You are alright togther,your score is {score}")
else:
    print(f"Your score is : {score}")




