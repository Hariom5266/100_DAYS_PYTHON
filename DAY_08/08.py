# 🍵, Hanji Kaise ho aap sabhi ,This is 8th day of Pyhton Challenge.I’m back and ready to code,Let's roll the code!

# ======================== Functions with inputs ======================== #

def greet():
    print("Hello")
    print("how do you do?")
    print("Isn;t the weather nice today?")

greet()

def greet2(name):
    print("Hello")
    print(f"How are you {name}?")
    
# parameter -- name of data # argument -- value of the data
    
greet2("Hariom Joshi")
greet2("Harish Joshi")

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Hariom Joshi","Ahemedabad")

greet_with(location="Ahemedabad",name="Hariom Joshi")

# ===================== how many paint need ===================== #
import math
def paint_wall(length,width,coverage):
    cans = (length*width)/coverage
    return math.ceil(cans)

length = int(input("Enter wall length?\n"))
width = int(input("Enter wall width?\n"))
coverage = 5
print("Number of cans you need for paint this wall is:",paint_wall(length=length,width=width,coverage=coverage))

# ===================== prime number cheker ===================== #
def check_prime(num):
    is_prime = True
    for i in range(2,num):
        if num % i==0:
            is_prime = False
    if is_prime:
     print("It's a prime number.")
    else:
        print("It's not a prime number.")
    
prime = int(input("Enter any number: "))
check_prime(prime)

















