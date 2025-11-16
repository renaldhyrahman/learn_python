import colorgram  # pyright: ignore[reportMissingImports]

colors = [
    (color.rgb[0], color.rgb[1], color.rgb[2])
    for color in colorgram.extract("image.jpg", 10)
]
print(colors)
