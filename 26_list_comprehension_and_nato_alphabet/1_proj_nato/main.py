import config as c
import pandas as pd  # type: ignore

# TODO-1: Create a dictionary in this format:
#         {"A": "Alfa", "B": "Bravo"}

# TODO-2: Create a list of the phonetic code words
#         from a word that the user inputs.

# Solution-1
df_nato = pd.read_csv(c.PATH_CSV)
dict_nato = {r.letter: r.code for _, r in df_nato.iterrows()}

# Solution-2
input_user = None
while input_user is None:
    input_user = input("Enter a word: ")
input_user = input_user.strip().upper()
print([dict_nato[letter] for letter in input_user])
