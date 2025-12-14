# FileNotFoundError  (File is not exists)
# with open("a_file.txt") as f:
#   f.read()


# KeyError (Key is not exists)
# a_dict = {"key": "value"}
# value = a_dict["not_key"]


# IndexError (Index is not exists)
# a_list = ["a", "b", "c"]
# fruit = a_list[20]


# NameError (Undefined)
# a_list = ["a", "b", "c"]
# fruit = something_else


# TypeError  (Data type error)
# text = "abc"
# text += 1


"""
try: Something that might cause an exception
except (<error1>, <error2>): if there was an exception
else: Do this if there were NO EXCEPTION
finally: Do this no matter what happens
"""


# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as msg:
#     print(f"Key {msg} does not exists")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     raise TypeError("This is custom error message.")


height = float(input("Height: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
weight = int(input("Weight: "))
bmi = weight / height**2
print(bmi)
