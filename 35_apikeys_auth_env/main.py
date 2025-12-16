import constants as cons
import requests


def get_forecast() -> list[dict[str, str | int]]:
    api_endpoint = cons.API.OWM_ENDPOINT.value
    api_endpoint += "/forecast"
    res = requests.get(
        url=api_endpoint,
        params={
            "lat": cons.Location.LATITUDE.value,
            "lon": cons.Location.LONGITUDE.value,
            "cnt": 4,
            "appid": cons.API.OWM_KEY.value,
        },
    )
    res.raise_for_status()
    data = res.json()["list"]
    return [
        {
            "id": el["weather"][0]["id"],
            "description": el["weather"][0]["description"],
            "dt_txt": el["dt_txt"],
        }
        for el in data
    ]


forecast = get_forecast()
for weather in forecast:
    if weather["id"] < 700:
        date, time = weather["dt_txt"].split(" ")
        print(f"{date} @ {time} :\nBring an umbrella.")
