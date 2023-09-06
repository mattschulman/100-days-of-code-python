import random
#from replit import clear
import hangman_art
import hangman_words
import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else: 
        _ = os.system('clear')

def interface():
    print("\n")
    print("Guessed Letters:")
    guesses.sort()
    for letter in guesses:
      print(letter, end=" ")
    print("\n")
      
    print(hangman_art.stages[lives])


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print("\n")
print(f"{' '.join(display)}")
print("\n")


guesses = []
while not end_of_game:
    interface()

    guess = input("Guess a letter: ").lower()

    clear()
  
    if guess not in guesses:
      guesses.append(guess)
    else:
      print(f"You already guessed {guess}.")
      print(f"{' '.join(display)}")
      continue

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
       #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"You guessed {guess}.  That is not in the word.  You lose a life.")
        if lives == 0:
            end_of_game = True
            print(hangman_art.stages[lives])
            print("\n")
            print("You lose.")
            print(f"The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # print("\n")
    # print("Guessed Letters:")
    # guesses.sort()
    # for letter in guesses:
    #   print(letter, end=" ")
    # print("\n")
      
    # print(hangman_art.stages[lives])