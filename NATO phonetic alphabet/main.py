import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(new_dict)

def generate_phenotic():
    user_word = input("Enter the word: ").upper()
    try:
        words_list = [new_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, Only letters in the aplhabet please.")
        generate_phenotic()
    else:
        print(words_list)

generate_phenotic()