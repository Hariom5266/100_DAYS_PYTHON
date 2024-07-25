# 🍵 , Hanji Kaise ho aap sabhi this is 5th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

fruits = ["apple","peach","pear"]

for fruit in fruits:
    print(fruit)
    print(fruit+"Pie")
    

# ================= Average Height of student ======================== #
heights_input = input("Enter the heights of students separated by spaces: ")
heights_str_list = heights_input.split()
heights_list = [int(height) for height in heights_str_list]
print(heights_list)

total_height = 0
count_student = 0
for height in heights_list:
    total_height+=height
    count_student+=1

print("Average height of student is :",total_height/count_student)

# ================= Highest score of student ======================== #
score_input = input("Enter the marks of students separated by spaces: ")
score_str_list = score_input.split()
score_list = [int(score) for score in score_str_list]
print(score_list)
max_score = 0
for score in score_list:
    if score > max_score:
        max_score = score
print("Max score is:",max_score)

# # ======================== range fucntion ======================== #
for number in range(1,10):
    print(number)
    
for number in range(1,11,3):
    print(number)

total = 0
for number in range(1,101):
    total+=number
# print(total)

# # ======================== add even number 1 to n ======================== #
n = int(input("Enter number which upto you want to add even number:\n"))
for number in range(1,n):
    if number % 2==0:
        print(number)
        
# ======================== add Odd number 1 to n ======================== #
n = int(input("Enter number which upto you want to add odd number:\n"))
for number in range(1,n):
    if number % 2!=0:
        print(number) 

# ======================== FizzBuzz Game ======================== #
for number in range(1,101):
    if number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0 and number%5==0:
        print("FizzBuzz")
    else:
        print(number)

    













