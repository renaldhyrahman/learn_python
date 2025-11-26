from pathlib import Path

# ##### Challenge d24 (Files and directory)
# Create a letter using starting_letter.docx
# Replace the ['name'] placeholder with the actual name.
#  Save the letters in the folder "ReadyToSend"

# ################### My solution


def create_letter(path: str, placeholder: str, insert_str: str):
    """Return a string, replace `placeholder` with `insert_str`"""

    with open(path, "r") as f:
        # Solution 1
        return f.read().replace(placeholder, insert_str)

        # Solution 2
        # return f.readline().replace(placeholder, insert_str) + f.read()

        # Solution 3
        # file_lines = f.readlines()
        # return "".join(
        #     [file_lines[0].replace(placeholder, insert_str)] + file_lines[1:]
        # )


def save_letter(path: str, file_name: str, content: str):
    """Write content to file
    (result will be saved to `path` + '/' + `file_name`)

    If path doesn't exist, will create path.

    If file_name already exists, the old file_name will be replaced.
    """

    Path(path).mkdir(parents=True, exist_ok=True)
    with open(f"{path}/{file_name}", "w") as f:
        f.write(content)


# ###################

path_names = "Input/Names/invited_names.txt"
path_letter = "Input/Letters/starting_letter.txt"
path_output = "Output/ReadyToSend"

with open(path_names, "r") as f:
    invited_names = f.read().split("\n")
    for name in invited_names:
        name = name.strip().capitalize()
        content = create_letter(
            path=path_letter, placeholder="[name]", insert_str=name
        )
        save_letter(
            path=path_output,
            file_name=f"letters_for_{name}.txt",
            content=content,
        )
