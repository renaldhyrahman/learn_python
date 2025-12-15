# ######################    TODO    ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# ######################  Solution  ######################


import datetime as dt

import constants as cons
import pandas as pd

# ######################    Func    ######################


def fetch_data():
    df_data = pd.read_csv(cons.Path.DATA.value)
    return df_data.to_dict(orient="records")


def send_mail(name: str, email: str):
    print(f"{name} = {email}")


# ######################    Run     ######################


list_data = fetch_data()
today = dt.date.today()
for data in list_data:
    if data["month"] == today.month and data["day"] == today.day:
        send_mail(data["name"], data["email"])
