# 🍵 , Hanji Kaise ho aap sabhi this is 25th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ===================== WORK WITH CSV ===================== #

# with open("./DAY_25/weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data)


# import csv
# with open("./DAY_25/weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     # print(data) # print obj
#     temprature = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temprature.append(int(row[1]))
#     print(temprature)
    
# ===================== WORK WITH PANDAS ===================== #
# use pandas.org for documentation

import pandas
data=pandas.read_csv("./DAY_25/weather_data.csv")
# print(data)

# print(data["temp"])

# ===================== DATA FRAMES & SERIES WORK WITH ROWS AND COLUMNS ===================== #

# print(type(data)) # dataframe

# DataFrames = whole one excel seet consider as a DataFrames in pandas
# Series = it is a single column of the file or table => day,temp,condition

# data_dict=data.to_dict() # convert csv to dictionary
# # print(data_dict)

# temp_list=data["temp"].to_list()
# print(temp_list)

# average=sum(temp_list)//len(temp_list)
# print(f"Average of temprature is : {average}")

# print(data["temp"].mean()) # it give average of the list
# print(data["temp"].max())

# Get Data in columns
# print(data["condition"])
# print(data.temp) # it is case sensitive

# Get data in Row
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()]) 

monday=data[data.day=="Monday"]
# print(monday.condition)
monday_temp=monday.temp[0]
print(monday_temp*9/5+32)

# Create a dataframe from scratech

data_dict={
    "students":["Any","James","Anglena"],
    "scores":[76,56,65]
}

data=pandas.DataFrame(data_dict)
# print(data)
data.to_csv("./DAY_25/new_data.csv")






