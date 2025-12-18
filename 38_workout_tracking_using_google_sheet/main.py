import datetime as dt
from typing import Any

import constants as const
import requests


def fetch_server_status() -> dict[str, Any]:
    """
    Check connection with `app.100daysofpython.dev`

    :return: JSON response from `app.100daysofpython.dev`
    :rtype: dict[str, Any]

    :raise: `requests.exceptions.HTTPError`
    if the API returns an unsuccessful status code.
    """
    endpoint = "/healthz"
    res = requests.get(
        url=const.API + endpoint,
        headers={
            "x-app-id": const.APP_ID,
            "x-app-key": const.APP_TOKEN,
        },
    )
    res.raise_for_status()
    return res.json()


def calc_calories(message: str) -> list[dict[Any, Any]]:
    """
    Calculate calories burned from a natural language exercise description,
    on `app.100daysofpython.dev` server

    :args:
      message: query of activity as plain message.
      (e.g. "I ran 2k today!")

    :return: A list extracted from `"exercises"` key of  JSON response
    from `app.100daysofpython.dev` server.

    :raise: `requests.exceptions.HTTPError`
    if the API returns an unsuccessful status code.
    """
    endpoint = "/v1/nutrition/natural/exercise"
    res = requests.post(
        url=const.PYTHON_API + endpoint,
        headers={
            "x-app-id": const.PYTHON_APP_ID,
            "x-app-key": const.PYTHON_APP_TOKEN,
        },
        json={"query": message},
    )
    res.raise_for_status()
    return res.json()["exercises"]


def record_activities(payload: dict[str, Any]):
    """
    Record activities on google sheet with `sheety` API.
    Will silently fail if payload `key` doesn't match
    google sheet column with `camelCase`.

    :raise: `requests.exceptions.HTTPError`
    if the API returns an unsuccessful status code.
    """
    endpoint = f"/{const.SHEETY_USERNAME}/myWorkouts/workouts"
    res = requests.post(
        url=const.SHEETY_API + endpoint,
        headers={"Authorization": const.SHEETY_TOKEN},
        json={
            "workout": payload,
        },
    )
    res.raise_for_status()
    print(res.text)


# res = fetch_server_status()
# print(res)
# input_activity = "I ran 2k today!"
input_activity = input("Tell me which exercises you did: ")
exercises = calc_calories(input_activity)
for exercise in exercises:
    payload = {
        # pre-populated cell: '21/07/2020
        "date": dt.date.today().strftime("%d/%m/%Y"),
        # pre-populated cell: 15:00:00 PM
        "time": dt.datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }
    record_activities(payload)
