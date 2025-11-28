# ##################  List Comprehension

"""zsh
❯ py
Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = [n+1 for n in range(1,5)]
>>> a
[2, 3, 4, 5]
>>> names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freedie']
>>> _names = [name[0] for name in names if name[0] != 'A' or name[0] != 'C']
>>> _names
['A', 'B', 'C', 'D', 'E', 'F']
>>> _names = [name[0] for name in names if name[0] == 'A']
>>> _names
['A']
>>> _names = [name[0] for name in names if 'e' == name]
>>> _names
[]
>>> _names = [name[0] for name in names if 'e' in name]
>>> _names
['A', 'B', 'C', 'D', 'F']
>>> _names = [name for name in names if 'e' in name]
>>> _names
['Alex', 'Beth', 'Caroline', 'Dave', 'Freedie']
>>> names[4] = 'Eleanor'
>>> names
['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freedie']
>>> _names = [name for name in names if 'e' in name]
>>> _names
['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freedie']
>>> _names = [name for name in names if 'a' in name]
>>> _names
['Caroline', 'Dave', 'Eleanor']
>>> _names = [name for name in names if len(name) < 5]
>>> _names
['Alex', 'Beth', 'Dave']
>>> uppercase = [name.uppercase() for name in names if len(name) > 4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'uppercase'
>>> uppercase = [name.upper() for name in names if len(name) > 4]
>>> uppercase
['CAROLINE', 'ELEANOR', 'FREEDIE']
>>> exit()
"""

# ##################  Dict Comprehension
"""zsh
❯ py
Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> names
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'names' is not defined
>>> names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freedie']
>>> students_scores = {name: 0 for el in names}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined. Did you mean: 'names'?
>>> students_scores = {name: 0 for name in names}
>>> students_scores
{'Alex': 0, 'Beth': 0, 'Caroline': 0, 'Dave': 0, 'Eleanor': 0, 'Freedie': 0}
>>> students_scores = {name: random.randint(0,100) for name in names}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'random' is not defined. Did you forget to import 'random'?
>>> import random
>>> students_scores = {name: random.randint(0,100) for name in names}
>>> students_scores
{'Alex': 62, 'Beth': 44, 'Caroline': 84, 'Dave': 7, 'Eleanor': 86, 'Freedie': 92}
>>> passed_students = {key: value for key,value in students_scores.items() if value > 59}
>>> passed_students
{'Alex': 62, 'Caroline': 84, 'Eleanor': 86, 'Freedie': 92}
>>>
"""  # noqa (E501)

# ##################  Iterate over a Pandas DataFrame

dict_student = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

import pandas as pd  # type: ignore # noqa (E402)

df_student = pd.DataFrame(dict_student)
# print(df_student)
"""zsh
❯ py main.py
  student  score
0  Angela     56
1   James     76
2    Lily     98
"""

# ##########  Normal Loop

for key, value in df_student.items():
    # print(key)
    """ "zsh
    ❯ py main.py
    student
    score
    """
    # print(value)
    """zsh
    ❯ py main.py
    0    Angela
    1     James
    2      Lily
    Name: student, dtype: object
    0    56
    1    76
    2    98
    Name: score, dtype: int64
    """
    # print(key, value)
    """zsh
    ❯ py main.py
    student 0    Angela
    1     James
    2      Lily
    Name: student, dtype: object
    score 0    56
    1    76
    2    98
    Name: score, dtype: int64
    """

# ##########  .iterrows()

for i, row in df_student.iterrows():
    # print(i)
    """zsh
    ❯ py main.py
    0
    1
    2
    """
    # print(row)  # row == Series
    """ zsh
    ❯ py main.py
    student    Angela
    score          56
    Name: 0, dtype: object
    student    James
    score         76
    Name: 1, dtype: object
    student    Lily
    score        98
    Name: 2, dtype: object
    """
    print(row.student)
    """zsh
    ❯ py main.py
    Angela
    James
    Lily
    """
