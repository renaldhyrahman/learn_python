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
while input_user is None or input_user == "":
    input_user = input("Enter a word: ").strip()
input_user = input_user.upper()
try:
    print([dict_nato[letter] for letter in input_user])
except KeyError:
    print("Unexpected Input.")
    print("Input must be `a word` contains only alphabet letters.")

"""txt
`Enter a word: test123` and
`Enter a word: test 123` (input > 1 word)
Will break the code,
solving it will require logics (more than 1 line logic) inside for loop,
in which will violate the topic of lecture
(list and dict comprehension).
So I am not bothering myself to fix this issue.
"""

# ##################  Sandbox

df_nato2 = pd.read_csv(c.PATH_CSV).set_index("letter")["code"]
# print(df_nato2)
"""zsh
❯ py main.py
letter
A        Alfa
B       Bravo
C     Charlie
D       Delta
E        Echo
F     Foxtrot
G        Golf
H       Hotel
I       India
J      Juliet
K        Kilo
L        Lima
M        Mike
N    November
O       Oscar
P        Papa
Q      Quebec
R       Romeo
S      Sierra
T       Tango
U     Uniform
V      Victor
W     Whiskey
X       X-ray
Y      Yankee
Z        Zulu
"""
dict_nato2 = df_nato2.to_dict()
# print(dict_nato2)
"""zsh
{
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie',
    'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
    'G': 'Golf', 'H': 'Hotel', 'I': 'India',
    'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
    'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
    'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
    'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee', 'Z': 'Zulu'
}
"""
# print(dict_nato2 == dict_nato) # True
