# BMI -- BODY MASS INDEX 
print("Welcome In BMI Calculator.")
weight = int(input("Enter Your Weight (Kg) : "))
height = float(input("Enter Your height (meter) : "))

BMI = (weight) / (height * height)
print("Your BMI is : " + str(BMI))