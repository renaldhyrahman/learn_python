# ######################   SMTPlib  ######################

# import smtplib

# import constants as cons

# using open and then close at the end

# connection = smtplib.SMTP(
#     host=cons.Smtp.HOST_1.value,
#     port=cons.Smtp.PORT_1.value,
# )
# connection.starttls()  # secure connection
# connection.login(
#     user=cons.Smtp.USER_1.value,
#     password=cons.Smtp.PWD_1.value,
# )
# connection.sendmail(
#     from_addr=cons.Smtp.USER_1.value,
#     to_addrs=cons.Smtp.USER_2.value,
#     msg="Subject:Hello\n\n" "This is the body of my email.",
# )
# connection.close()


# using 'with' keyword

# with smtplib.SMTP(
#     host=cons.Smtp.HOST_1.value,
#     port=cons.Smtp.PORT_1.value,
# ) as connection:
#     connection.starttls()  # SMTP encryption
#     connection.login(
#         user=cons.Smtp.USER_1.value,
#         password=cons.Smtp.PWD_1.value,
#     )
#     connection.sendmail(
#         from_addr=cons.Smtp.USER_1.value,
#         to_addrs=cons.Smtp.USER_2.value,
#         msg="Subject:Test 'with' keyword\n\n"
#         "This is the body of the message.",
#     )


# ######################  DateTime  ######################

import datetime as dt

now = dt.datetime.now()
print(f"now = {now}, type = {type(now)}")
year = now.year
print(f"year = {year}, type = {type(year)}")
month = now.month
print(f"month = {month}, type = {type(month)}")
day_of_week = now.weekday()  # monday = 0, sunday = 6
print(f"weekday = {day_of_week}, type = {type(day_of_week)}")

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)
