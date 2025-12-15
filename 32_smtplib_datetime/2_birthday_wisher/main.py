# ######################    TODO    ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# ######################  Solution  ######################


import datetime as dt
import os
import random as r
import smtplib

import constants as cons
import pandas as pd

# ######################    Func    ######################


def fetch_data():
    df_data = pd.read_csv(cons.Path.DATA.value)
    return df_data.to_dict(orient="records")


def get_random_letter(name: str):
    letters_dir = cons.Path.LETTERS_DIR.value
    files = os.listdir(letters_dir)
    path_random_letter = f"{letters_dir}/{r.choice(files)}"
    with open(path_random_letter, "r") as f:
        letter = f.read()
        letter = letter.replace("[NAME]", name)
        return letter


def send_mail(name: str, email: str):
    letter = get_random_letter(name)
    with smtplib.SMTP(
        host=cons.Smtp.HOST.value,
        port=cons.Smtp.PORT.value,
    ) as connection:
        connection.starttls()
        connection.login(
            user=cons.Smtp.USER.value,
            password=cons.Smtp.PWD.value,
        )
        connection.sendmail(
            from_addr=cons.Smtp.USER.value,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{letter}",
        )
    print(f"email sent to: {email}")


# ######################    Run     ######################


list_data = fetch_data()
today = dt.date.today()
for data in list_data:
    if (data["month"], data["day"]) == (today.month, today.day):
        send_mail(data["name"], data["email"])
