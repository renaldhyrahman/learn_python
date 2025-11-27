# Challenge: Create a csv which contain `Fur Color` and `Count`

# ############### My Solution

import pandas as pd  # type: ignore

path_csv = (
    "2_data_analysis/"
    "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251127.csv"
)
path_result = "2_data_analysis/squirel_count.csv"

df_squirrel = pd.read_csv(path_csv)

# dict_color = {
#     "Fur Color": [],
#     "Count": [],
# }

# for i, row in df_squirrel.iterrows():
#     _color = row["Primary Fur Color"]
#     if not type(_color) is str:
#         continue
#     list_color = dict_color["Fur Color"]
#     list_count = dict_color["Count"]
#     if _color not in list_color:
#         list_color.append(_color)
#         list_count.append(0)
#     index_color = list_color.index(_color)
#     list_count[index_color] += 1


# df_result = pandas.DataFrame(dict_color)
# df_result.to_csv(path_result)


# ############### Pythonic Solution


# ######## Debug

debug_result = df_squirrel["Primary Fur Color"].value_counts()
# print(result)
# CONSOLE OUTPUT:
#
# Primary Fur Color
# Gray        2473
# Cinnamon     392
# Black        103
# Name: count, dtype: int64
#

debug_result = debug_result.reset_index()
# print(result)
# CONSOLE OUTPUT:
#
#   Primary Fur Color  count
# 0              Gray   2473
# 1          Cinnamon    392
# 2             Black    103
#

# print(result.columns)
# CONSOLE OUTPUT:
#
# Index(['Primary Fur Color', 'count'], dtype='object')
#

debug_result.columns = ["Fur Color", "Count"]
# print(debug_result.columns)
# CONSOLE OUTPUT:
#
# Index(['Fur Color', 'Count'], dtype='object')
#

# ########

alt_result = df_squirrel["Primary Fur Color"].value_counts().reset_index()
alt_result.columns = ["Fur Color", "Count"]

# alt_result.to_csv(path_result)
