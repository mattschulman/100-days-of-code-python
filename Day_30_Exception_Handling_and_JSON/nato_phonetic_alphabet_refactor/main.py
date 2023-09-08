import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Dictionary comprehension to get the letter and code from each row in the nato_data DataFrame
nato_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()} 

def generate_phonetic_list(word):
    #Try to generate the list, if there's a character that's not a letter, print a message and call go() to prompt the user to reinput
    try:
        phonetic_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet, please.")
        go()
    else:
        #Input is good.  Print the list
        print(phonetic_list)

def go():
    #Get the word from the user and pass into generate_phonetic_list()
    response = input("Enter a word: ").upper()
    generate_phonetic_list(response)


#main function
go()
