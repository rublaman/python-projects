import pandas as pd

# Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_phonetic_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_dictionary = {row["letter"]: row["code"] for (index, row) in nato_phonetic_dataframe.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.

def nato_alphabet():
    user_input = input("What is your name: ").upper()

    try:
        result = [nato_phonetic_dictionary[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_alphabet()
    else:
        print(result)

nato_alphabet()