from datetime import date, timedelta
from typing import Any

import constants as const
import requests as req

# ######################   Func   ######################


def create_user(user: tuple[str, str]) -> dict[str, Any]:
    """
    Create pixela user account.

    Returns `json` response from the Pixela API.

    Args:
      user: Tuple of (username, user token).

    Raises:
      requests.exceptions.HTTPError: If the API returns
                                     an unsuccessful status code.
    """
    username, usertoken = user
    res = req.post(
        url=const.PIXELA_API,
        json={
            "token": usertoken,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        },
    )
    print(res.text)
    res.raise_for_status()
    return res.json()


def create_graph(
    user: tuple[str, str],
    graph: dict[str, str],
) -> dict[str, Any]:
    """
    Use `graph` to create and define pixela graph.

    Returns `json` response from the Pixela API.

    Args:
      user: Tuple of (username, user token).
      graph: A dictionary, expecting key (required):
      `"id"`: ID for identifying graph.
      `"name"`: Name of the graph.
      `"unit"`: Unit of quantity recorded.
      `"type"`: Type of quantity, only support `"int"` or `"float"`
      `"color"`: Defines the display color. Color kind:
        - "shibafu" (green)
        - "momiji" (red)
        - "sora" (blue)
        - "ichou" (yellow)
        - "ajisai" (purple)
        - "kuro" (black)

    Raises:
      requests.exceptions.HTTPError: If the API returns
                                     an unsuccessful status code.
    """
    username, usertoken = user
    endpoint = f"/{username}/graphs"
    res = req.post(
        url=const.PIXELA_API + endpoint,
        headers={"X-USER-TOKEN": usertoken},
        json={
            # intentional to raise KeyError if there is missing key.
            "id": graph["id"],
            "name": graph["name"],
            "unit": graph["unit"],
            "type": graph["type"],
            "color": graph["color"],
        },
    )
    print(res.text)
    res.raise_for_status()
    return res.json()


def record_pixel(
    user: tuple[str, str],
    graph_id: str,
    date: str,
    quantity: int | float,
) -> dict[str, Any]:
    """
    Record the `quantity` (pixel) on `date` to `graph_id` on Pixela.

    Returns `json` response from the Pixela API.

    Args:
      user: Tuple of (username, user token).
      graph_id: ID of the pixela's graph.
      date: Date in format `YYYYMMDD`
      quantity: Quantity to be recorded,
               must match the `type` when the graph is created.
               If it was `"int"` then it can't be float.

    Raises:
      requests.exceptions.HTTPError: If the API returns
                                     an unsuccessful status code.
    """
    username, usertoken = user
    endpoint = f"/{username}/graphs/{graph_id}"
    res = req.post(
        url=const.PIXELA_API + endpoint,
        headers={"X-USER-TOKEN": usertoken},
        json={
            "date": date,
            "quantity": f"{quantity}",
        },
    )
    print(res.text)
    res.raise_for_status()
    return res.json()


def update_pixel(
    user: tuple[str, str],
    graph_id: str,
    date: str,
    quantity: int | float,
) -> dict[str, Any]:
    """
    Update the pixela's record of `quantity` (pixel) in `graph_id` on `date`.

    Returns `json` response from the Pixela API.

    Args:
      user: Tuple of (username, user token).
      graph_id: ID of the pixela's graph.
      date: Date in format `YYYYMMDD`
      quantity: Quantity to be updated,
               must match the `type` when the graph is created.
               If it was `"int"` then it can't be float.

    Raises:
      requests.exceptions.HTTPError: If the API returns
                                     an unsuccessful status code.
    """
    username, usertoken = user
    endpoint = f"/{username}/graphs/{graph_id}/{date}"
    res = req.put(
        url=const.PIXELA_API + endpoint,
        headers={"X-USER-TOKEN": usertoken},
        json={"quantity": f"{quantity}"},
    )
    print(res.text)
    res.raise_for_status()
    return res.json()


def delete_pixel(
    user: tuple[str, str],
    graph_id: str,
    date: str,
) -> dict[str, Any]:
    """
    Delete the pixela's record of `quantity` (pixel) in `graph_id` on `date`.

    Returns `json` response from the Pixela API.

    Args:
      user: Tuple of (username, user token).
      graph_id: ID of the pixela's graph.
      date: Date in format `YYYYMMDD`

    Raises:
      requests.exceptions.HTTPError: If the API returns
                                     an unsuccessful status code.
    """
    username, usertoken = user
    endpoint = f"/{username}/graphs/{graph_id}/{date}"
    res = req.delete(
        url=const.PIXELA_API + endpoint,
        headers={"X-USER-TOKEN": usertoken},
    )
    print(res.text)
    res.raise_for_status()
    return res.json()


# ######################    APP   ######################


user = (const.USER_USERNAME, const.USER_TOKEN)
create_user(user)
graph = {
    "id": "graph1",
    "name": "cycling",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
# create_graph(user, graph)

date_today = date.today()
date_today_str = date_today.strftime("%Y%m%d")

date_yesterday = date.today() - timedelta(days=1)
date_yesterday_str = date_yesterday.strftime("%Y%m%d")

date_test = (date.today() - timedelta(days=2)).strftime("%Y%m%d")

# record_pixel(
#     user=user,
#     graph_id=graph["id"],
#     date=date_test,
#     quantity=75,
# )

# update_pixel(
#     user=user,
#     graph_id=graph["id"],
#     date=date_test,
#     quantity=25,
# )


delete_pixel(
    user=user,
    graph_id=graph["id"],
    date=date_test,
)
