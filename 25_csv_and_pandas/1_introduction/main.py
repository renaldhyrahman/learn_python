path_csv = "1_introduction/weather_data.csv"

# ############### Challenge 1
#
# Open the weather_data.csv.
# Use `.readlines()` to create a list named `data`
# that contains the values from the .csv file.


def read_csv(path):
    with open(path, "r") as f:
        return [el.split(",") for el in f.read().split("\n")]


c1 = read_csv(path_csv)
# print(c1)

# ############### Using module (csv (python))
# Challenge 2
# Using module create a temperature (list) which contains
# all the  temperatures from data,
# the temperature number must be an integer not a string

import csv  # noqa (E402)

with open(path_csv) as f:
    data = csv.reader(f)
    # temperature = [row[1] for row in data[1:]]
    temperature = []
    for i, row in enumerate(data):
        # print(row == c1[i])  # True
        # print(row is c1)  # False
        if not i:
            continue
        temperature.append(int(row[1]))
    # print(temperature)


# ############### Using module (pandas (pip))

import pandas  # type: ignore # noqa (E402)

data_pandas = pandas.read_csv(path_csv)
# print(data_pandas)
# print(data_pandas["temp"])

# print(type(data_pandas) is object)  # False

# print(type(data_pandas))  # <class 'pandas.core.frame.DataFrame'>
# Every single sheet in csv or the data table,
# will be considered a Dataframe (object)

# print(type(data_pandas["temp"]))  # <class 'pandas.core.series.Series'>
# The Series (object), basically equivalent to list,
# kind of like a single collumn in csv.

dict_data_pandas = data_pandas.to_dict()
# print(dict_data_pandas)  # {'day': {0: 'Monday', 1: 'Tuesday',...}, ...}

list_data_pandas_temp = data_pandas["temp"].to_list()
# print(list_data_pandas_temp)  # [12, 14, 15, 14, 21, 22, 24]
# print(type(list_data_pandas_temp[0]))  # <class 'int'>


# Challenge 3 -
# Print the average temp


def get_average_from_csv(path: str, col: str):
    """Returns float if `col` in csv is a number,

    otherwise return None"""

    try:
        avg = pandas.read_csv(path)[col].mean()
        return round(avg, 2)
    except (KeyError, FileNotFoundError, TypeError):
        return
    # except FileNotFoundError:
    #     print(f"FileNotFoundError: path (`{path}`) is not found.")
    # except KeyError:
    #     print(f"KeyError: col (`{col}`) is not found in csv.")
    # except TypeError:
    #     print(f"TypeError: `{col}` in the csv is not a number.")
    # except Exception as e:
    #     print(type(e), e)
    #     raise


c3 = get_average_from_csv(path=path_csv, col="temp")
# print(c3)

# Challenge 4 -
# Get the max value of temp


def get_max_value_from_csv(path: str, col: str):
    return pandas.read_csv(path)[col].max()


c4 = get_max_value_from_csv(path=path_csv, col="temp")
# print(c4)


# ######## Pandas: Get data in column


# print(data_pandas["condition"])
# print(data_pandas.condition)
# print(data_pandas["condition"] == data_pandas.condition)

# ########

df_weather = data_pandas  # df (DataFrame)

# ######## Pandas: Get data in row
# print(df_weather[df_weather.day == "Monday"])


# Challenge 5 -
# Pull the row where the temp is at maximum


c5 = df_weather[df_weather.temp == df_weather.temp.max()]
# print(c5)


# monday = df_weather[df_weather.day == "Monday"]
# print(monday.condition)  # 0    Sunny

# Challenge 6 -
# Convert Monday's temp to fahrenheit


def c_to_f(number: int | float):
    return (number * 1.8) + 32


c6 = c_to_f(df_weather[df_weather.day == "Monday"].temp)
# print(c6)


# ######## Create dataframe

dict_data = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
df_data = pandas.DataFrame(data=dict_data)
# print(df_data)

# ######## exports df to csv (write)

path_export = "1_introduction/new_data.csv"
df_data.to_csv(path_export)
