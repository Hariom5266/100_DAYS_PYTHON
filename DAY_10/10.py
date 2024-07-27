# 🍵, Hanji Kaise ho aap sabhi ,This is 10th day of Pyhton Challenge.I’m back and ready to code,Let's roll the code!

# ==================== Functions with output ==================== #

# simple function
# function with inputs
# function with output --> it like machine that fill empty nottle by milk

def my_function():
    result = 3*2
    return result

print(my_function())

def format_name(f_name,l_name):
    # it convert name into title tezt
    full_name = f_name+" "+l_name
    full_name=full_name.title()
    # print(full_name)
    return full_name
    
full_name_of_user = format_name("hAriOM","JOSHI")
print(full_name_of_user)

output = len("Hariom")
print(output)

# ==================== Return Multiple Values ==================== #

def format_name(f_name,l_name):
    if f_name =="" or l_name=="":
        return "You didn't provide valid inputs."
    full_name = f_name+" "+l_name
    full_name=full_name.title()
    # print(full_name)
    return full_name
    
full_name_of_user = format_name("hAriOM","JOSHI")
print(full_name_of_user)
full_name_of_user = format_name("","")
print(full_name_of_user)

# ==================== Days in Month ==================== #

def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    month_days=[31,28,31,30,31,20,31,31,20,31,20,31]
    if month==2 and is_leap(year):
        return 29
    else:
        return month_days[month-1]
    
print("This is a how many days in month calculator...!")
year = int(input("Enter a year : "))
month=int(input("Enter a month : "))
days=days_in_month(year=year,month=month)
print(days)
        
# ==================== Docstring ==================== #

#Docstring --> means when we have suggestions in vscode than we have it documentation, we can implement it using """Docstring content write here"""

#also docstring use as a multiline comments.

def format_name(f_name,l_name):
    """Take a first and last name and format it to
        return the title case version of the name.
    """
    if f_name =="" or l_name=="":
        return "You didn't provide valid inputs."
    full_name = f_name+" "+l_name
    full_name=full_name.title()
    # print(full_name)
    return full_name
    
full_name_of_user = format_name("hAriOM","JOSHI")
print(full_name_of_user)














