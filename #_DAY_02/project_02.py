# PROJECT _ 2 --> Tip Calculator

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $ : "))
tip = int(input("How much tip would you like to give ? 10, 12, or 15 ? : "))
people = int(input("How many people to split the bill ? :"))

tip_as_percenge = tip / 100
toatal_tip_amount = bill * tip_as_percenge
total_bil = bill + toatal_tip_amount
bill_per_person = total_bil / people
final_amount = round(bill_per_person , 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each Person should pay : ${final_amount}")



