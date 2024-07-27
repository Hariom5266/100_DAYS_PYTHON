# 🍵, Hanji Kaise ho aap sabhi ,This is 9th day of Pyhton Challenge.I’m back and ready to code,Let's roll the code!


# ==================== Dictionary & Nesting ==================== #

# #dictionary -- work like real life dictionary very useful
# #two part of dictionary key and associated value table

programming_dictionary={
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again."
}

#Reterive data from dictionary.
print(programming_dictionary['Bug'])

#Adding new item to dictionary.
programming_dictionary["Variable"]="Container that contains values"
print(programming_dictionary["Variable"])

# #create a empty dictionart
empty_dictionary={}

# #wipe an existing dictionary
# programming_dictionary={}
# print(programming_dictionary)

#Edit an item in dictionary
programming_dictionary["Bug"] = "This is a Bug."
print(programming_dictionary)

#Loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

# ==================== Student test score ==================== #

student_score = {
    "Hari":99,
    "ashish":88,
    "rahul":70,
    "manthan":50,
    "om":40,
    "HC JOSHI":100
}

student_grades={}

for student in student_score:
    score = student_score[student];
    if score>90:
        student_grades[student]="Overstanding"
    elif score>80:
        student_grades[student]="Exceeds Expectations"
    elif score>70:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"

for student in student_grades:
    print(student,end=":")
    print(student_grades[student])

# ==================== Nesting ==================== #

#
# {
#     key : [list],
#     key2:{Dict}
# }
#

capitals={
    "France":"Paris",
    "Inida":"Delhi"
}

#nesting a dist in a dictionary

travel_log={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"],
}

travel_log={
    "France":{"cities_visited":["Paris","Lille","Dijon"],"total_visits":5},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5},
}

#nesting dictionary in a list

travel_log2 = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 5
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    }
]

# ==================== travell log challenge ==================== #

country = input("Type country name:\n")
visits = int(input("Enter how many times you visited:\n"))
list_of_cities = input("Enter list of cities visited (separated by commas):\n").split(",")

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 5
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    }
]

def add_new_country(name, time_visited, cities_visited):
    new_country = {}  # Corrected to initialize as a dictionary
    new_country["country"] = name
    new_country["total_visits"] = time_visited
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)

print(travel_log)

















