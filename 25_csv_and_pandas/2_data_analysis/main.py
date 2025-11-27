# Task: Create a csv which contain `Fur Color` and `Count`

import pandas  # type: ignore

path_csv = (
    "2_data_analysis/"
    "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251127.csv"
)
path_result = "2_data_analysis/squirel_count.csv"

df_squirrel = pandas.read_csv(path_csv)

dict_color = {
    "Fur Color": [],
    "Count": [],
}

for i, row in df_squirrel.iterrows():
    _color = row["Primary Fur Color"]
    if not type(_color) is str:
        continue
    list_color = dict_color["Fur Color"]
    list_count = dict_color["Count"]
    if _color not in list_color:
        list_color.append(_color)
        list_count.append(0)
    index_color = list_color.index(_color)
    list_count[index_color] += 1


df_result = pandas.DataFrame(dict_color)
df_result.to_csv(path_result)
