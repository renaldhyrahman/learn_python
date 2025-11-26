# ########    File system   ########
file_path = "my_file.txt"
# ########    Read
# # Open the file
# my_file = open(file_path)
# # Read the file
# contents_1 = my_file.read()
# # Print the file
# print(contents_1)
# # Close the file (Free up resource)
# my_file.close()

# With keyword (no need to use .close())
with open(file_path, mode="r") as file:
    contents = file.read()
    print(contents)

# # ########    Write
# # Replace (mode='w')
# with open(file_path, mode="w") as f:
#     contents = "New Text from main.py"
#     f.write(contents)
# # Append
with open(file_path, mode="a") as f:
    contents = "\nNew Text from main.py"
    f.write(contents)
