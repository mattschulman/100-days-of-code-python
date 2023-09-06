import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#Dictionary comprehension to get the letter and code from each row in the nato_data DataFrame
nato_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()} 


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

phonetic_list = [nato_dict[letter] for letter in user_word]
# #Use a list comprehension to break the user_word list into a string of letters
# user_letters = [letter for letter in user_word]

# #Using a dictionary comprehension, get the letter, and the code (from the nato_letters dict based using the letter as key)
# #from looping through the letters in the user_letters list - if the letter is one of the nato_dict keys
# phonetic_spelling = {letter:nato_dict[letter] for letter in user_letters if letter in nato_dict.keys() }

# #use a list comprehension to get the code from the phoenetic spelling dictionary values
# phonetic_letters = [code for code in phonetic_spelling.values()]
print(phonetic_list)