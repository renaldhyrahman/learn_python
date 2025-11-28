# ##################  *args


def add(*args: int | float):
    try:
        return sum(args)
    except TypeError:
        print("TypeError: args must be a number (integer or float)")


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, ["asda"]))


# ##################  **kwargs


# kwargs = KeyWord ARGuments
def calculate(n: int | float, **kwargs):
    # for k, v in kwargs.items():
    #     pass
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


# print(calculate(2, add=3, multiply=5))  # 25


# Create Class with multiple optional arguments
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)  # None

# ##################  playground
