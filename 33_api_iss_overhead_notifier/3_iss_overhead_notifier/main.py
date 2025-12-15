import datetime as dt

import constants as cons
import requests

res = requests.get(
    url=cons.API,
    params={
        "lat": cons.LATITUDE,
        "lng": cons.LONGITUDE,
        "formatted": 0,
    },
)
res.raise_for_status()
data = res.json()
sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
sunset = data["results"]["sunset"].split("T")[1].split("+")[0]
time_now = dt.datetime.now().strftime("%H:%M:%S")
print(sunrise, sunset)
print(time_now)
