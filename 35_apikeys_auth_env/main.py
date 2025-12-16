import constants as cons
import requests


def get_forecast() -> list[dict[str, str]]:
    api_endpoint = cons.API_WEATHER
    api_endpoint += "/forecast"
    res = requests.get(
        url=api_endpoint,
        params={
            "lat": cons.Location.LATITUDE.value,
            "lon": cons.Location.LONGITUDE.value,
            "appid": cons.API_KEY_WEATHER,
        },
    )
    res.raise_for_status()
    data = res.json()["list"]
    return [
        {
            "id": el["weather"][0]["id"],
            "description": el["weather"][0]["description"],
        }
        for el in data
    ]


forecast = get_forecast()
print(forecast)
print(len(forecast))
