import colorgram as c  # pyright: ignore[reportMissingImports]


def get_palette(img_path: str, n_colors: int):
    """Return: list of rgb tuples ([ (9, 123, 46), ... ])

    Dependecies: colorgram
    """
    return [
        (color.rgb[0], color.rgb[1], color.rgb[2])
        for color in c.extract(img_path, n_colors)
    ]


colors = get_palette("images.jpg", 30)

print(colors)
