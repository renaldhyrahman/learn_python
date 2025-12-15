import datetime as dt
import smtplib
import time

import constants as cons
import requests


def is_iss_overhead():
    res = requests.get(cons.API_ISS_LOC)
    res.raise_for_status()
    data = res.json()
    iss_lng = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])
    if (
        abs(iss_lng - cons.LONGITUDE) <= cons.DELTA_ISS_OVERHEAD
        and abs(iss_lat - cons.LATITUDE) <= cons.DELTA_ISS_OVERHEAD
    ):
        return True
    return False


def is_past_sunset():
    res = requests.get(
        url=cons.API_SUNSET,
        params={
            "lat": cons.LATITUDE,
            "lng": cons.LONGITUDE,
            "formatted": 0,
            "tzid": cons.TZID,
        },
    )
    res.raise_for_status()
    data = res.json()
    sunset = data["results"]["sunset"]
    sunset = dt.datetime.fromisoformat(sunset).time()
    time_now = dt.datetime.now().time()
    if time_now > sunset:
        return True
    return False


def notifier(receiver: str):
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
            to_addrs=receiver,
            msg="Subject:ISS is visible\n\n"
            "Go outside and look above, ISS should be visible.",
        )


def is_iss_overhead_and_visible():
    if not is_iss_overhead():
        return print("ISS is not overhead")
    if not is_past_sunset():
        return print("ISS is overhead but not past sunset")
    notifier(cons.Smtp.RECEIVER.value)


def recursive(second: int):
    is_iss_overhead_and_visible()
    time.sleep(second)
    recursive(second)


recursive(60)
