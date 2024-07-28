# 🍵 , Hanji Kaise ho aap sabhi this is 13th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# =================== Debugging Exercise 1 =================== #

number = int(input("Enter a number: "))
if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# =================== Debugging Exercise 2 -- Leap year =================== #

year = int(input())

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap year.")
else:
    print("Not Leap Year.")

# =================== Debugging Exercise 3 --FizzBuzz =================== #

target = int(input())
for number in range(1,target+1):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)
            





