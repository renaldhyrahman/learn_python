import constants as const
import requests


def get_forecast() -> list[dict[str, str | int]]:
    api_endpoint = const.OpenWeatherMap.API.value
    api_endpoint += "/forecast"
    res = requests.get(
        url=api_endpoint,
        params={
            "lat": const.Location.LATITUDE.value,
            "lon": const.Location.LONGITUDE.value,
            "cnt": 4,
            "appid": const.OpenWeatherMap.TOKEN.value,
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


def send_telegram(message: str):
    url = const.Telegram.BOT_API.value + const.Telegram.BOT_TOKEN.value
    url += "/sendMessage"
    res = requests.post(
        url=url,
        json={
            "chat_id": const.Telegram.CHAT_ID.value,
            "text": message,
        },
    )
    res.raise_for_status()


forecast = get_forecast()
will_rain = False
for weather in forecast:
    if weather["id"] < 700:
        will_rain = True
if will_rain:
    message = "It's gonna rain today.\nRemember to bring an umbrella."
    send_telegram(message)
