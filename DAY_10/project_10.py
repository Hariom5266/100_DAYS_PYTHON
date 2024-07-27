# 🍵, Hanji Kaise ho aap sabhi ,This is 10th day of Pyhton Challenge.I’m back and ready to code,Let's roll the code!

# ==================== Calculator ==================== #

from art import logo
print(logo)

#Add
def add(n1,n2):
    return n1+n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Subtract
def subtract(n1,n2):
    return n1-n2

#Divide
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
# should_continue=True

# while should_continue:
operation_symbol = input("Pick an operation from the line above: ")    
num2 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# difference betwen print and return  when i should use return and when use print in fnc
'''when you want to use one fnc output to the another then use return otherwise use print'''

operation_symbol = input("Pick an operation from the line above: ")    
num3 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1,num2),num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

# ================================ version ---> 2 ============================= #

from art import logo
print(logo)

#Add
def add(n1,n2):
    return n1+n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Subtract
def subtract(n1,n2):
    return n1-n2

#Divide
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:
        operation = input("Pick an operation from the line above: ")    
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue=False
            calculator()

calculator()
