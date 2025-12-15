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
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise, sunset)
print(dt.datetime.now())
