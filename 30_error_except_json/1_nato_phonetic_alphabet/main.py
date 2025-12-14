import pandas

PATH_CSV = "nato_phonetic_alphabet.csv"

data = pandas.read_csv(PATH_CSV)

phonetic_dict = {row.letter: row.code for (i, row) in data.iterrows()}

is_input_correct = False
while not is_input_correct:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_input_correct = True
print(output_list)
