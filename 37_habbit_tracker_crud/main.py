import constants as const
import requests as req

# ######################   Func   ######################


def create_user(user: tuple[str, str]) -> dict[str, str]:
    """
    Create pixela user account.

    Raises an HTTPError, if one occurred.

    Returns a response from api as dict if success.

    Args:
      user: A tuple consist of `username` and `user token`
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
    res.raise_for_status()
    return res.json()


def create_graph(
    user: tuple[str, str],
    graph: dict[str, str],
) -> dict[str, str]:
    """
    Use `graph` to create and define pixela graph.

    Raises an HTTPError, if one occurred.

    Returns a response from api as dict if success.

    Args:
      user: A tuple consist of `username` and `user token`
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


# ######################    APP   ######################


user = (const.USER_USERNAME, const.USER_TOKEN)
# create_user(user)
graph = {
    "id": "graph1",
    "name": "cycling",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
create_graph(user, graph)
