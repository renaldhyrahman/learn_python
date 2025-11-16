import colorgram as c  # pyright: ignore[reportMissingImports]


def get_palette(img_path: str, n_colors: int):
    """
    Return: list of rgb tuples ([ (9, 123, 46), ... ])

    Dependecies: colorgram.py 1.2.0
    """
    return [
        (color.rgb.r, color.rgb.g, color.rgb.b)
        for color in c.extract(img_path, n_colors)
    ]
