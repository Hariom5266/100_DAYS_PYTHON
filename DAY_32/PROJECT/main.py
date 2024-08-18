# Birthday Wisher

import datetime as dt
import pandas as pd
import smtplib

# Get the current datetime
today = dt.datetime.now()

# Open the birthday_data file
birthday_data = pd.read_csv("./DAY_32/PROJECT/birthday_data.csv")
# print(birthday_data)

# My Email Account
MY_EMAIL = "hariextra3366@gmail.com"
PASSWORD="password"

for index,row_data in birthday_data.iterrows():
    # print(index,row_data)
    name = row_data['name']
    email = row_data['email']
    day = row_data['day']
    month = row_data['month']
    
    if month == today.month and day == today.day:
        # Open my_email format
        with open("DAY_32/PROJECT/email_format.txt") as email_format:
            content_email=email_format.read()
            send_email = content_email.replace('[Name]', name)
            # print(send_email)
        
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            
            # Email headers and body
            subject = f"🎂 Happy Birthday, {name}!"
            body = f"{send_email}"

            # Send the email
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=email,msg=f"Subject:{subject}\n\n{body}".encode('UTF-8'))
    