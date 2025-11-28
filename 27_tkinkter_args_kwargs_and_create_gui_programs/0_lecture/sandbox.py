# ##################  *args


def add(*args: int | float):
    try:
        return sum(args)
    except TypeError:
        print("TypeError: args must be a number (integer or float)")


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, ["asda"]))

# ##################
