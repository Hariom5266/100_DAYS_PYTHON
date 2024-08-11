import pandas 
data=pandas.read_csv("C:/Users/Lenovo/Desktop/01_HC_JOSHI/Work/100_DAYS_OF_PYTHON/DAY_25/data.csv")

grey_squirrels_count=len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count=len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"] == "Black"])



print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict={
    "Fur Color":["Gray","Cinnmon","Black"],
    "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df=pandas.DataFrame(data_dict)
df.to_csv("C:/Users/Lenovo/Desktop/01_HC_JOSHI/Work/100_DAYS_OF_PYTHON/DAY_25/squirral_count.csv")


