# import smtplib

# my_email = "hariextra3366@gmail.com"
# password="password"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() # tls --> Transfer layer Security # Make connection secure
#     connection.login(user=my_email,password=password)

#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="hariextra3366@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

# # connection.close() # We can avoide this line using with keyword

import datetime as dt

now=dt.datetime.now() # Datetime object
year=now.year # int
month=now.month
day_of_week=now.weekday() # 0 to 6 respect to day, week started at 0 index as a monday
print(day_of_week)
if year == 2024:
    print("I'm back in 2024")
# print(now)

date_of_birth=dt.datetime(year=2008,month=8,day=2,hour=8)
print(date_of_birth)



