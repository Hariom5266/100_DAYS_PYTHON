import smtplib 
import datetime as dt
import random

MY_EMAIL = "hariextra3366@gmail.com"
PASSWORD="password"

now = dt.datetime.now()
day=now.weekday()

if day==6:
        with open("./DAY_32/quotes.txt") as quotes_file:
            quote=quotes_file.readlines()
            # print(type(quote))
            
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=PASSWORD)
        
                random_quote=random.choice(quote)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject:Warrior_Devloper\n\n{random_quote}"
                )