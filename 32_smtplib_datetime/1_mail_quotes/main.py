import calendar
import datetime as dt
import random as r
import smtplib

import constants as cons

# ######################    Func   ######################


def fetch_quotes():
    with open(cons.PATH_QUOTES, "r") as f:
        quotes = []
        for row in f:
            quotes.append(row)
        return quotes


def send_mail_quote(
    quote: list[str],
    receiver: str,
    subject: str = "From Python",
):
    with smtplib.SMTP(
        host=cons.Smtp.HOST_1.value,
        port=cons.Smtp.PORT_1.value,
    ) as connection:
        connection.starttls()
        connection.login(
            user=cons.Smtp.USER_1.value,
            password=cons.Smtp.PWD_1.value,
        )
        connection.sendmail(
            from_addr=cons.Smtp.USER_1.value,
            to_addrs=receiver,
            msg=f"Subject:{subject}\n\n{r.choice(quote)}",
        )


# ######################    Run    ######################


quotes = fetch_quotes()
weekday_send_mail = dt.datetime.now().weekday()
day_send_mail = calendar.day_name[weekday_send_mail]

if dt.datetime.now().weekday() == weekday_send_mail:
    send_mail_quote(
        quote=quotes,
        receiver=cons.Smtp.USER_2.value,
        subject=f"{day_send_mail} Quotes",
    )
