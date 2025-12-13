import random as r

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def random_caps(letter):
    return r.choice([letter, letter.upper()])


def generate_password():
    result = []
    result.extend(
        [random_caps(r.choice(letters)) for _ in range(r.randint(8, 10))]
    )
    result.extend([r.choice(symbols) for _ in range(r.randint(2, 4))])
    result.extend([r.choice(numbers) for _ in range(r.randint(2, 4))])
    r.shuffle(result)
    return "".join(result)
