#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

def validate_guess(guess,number):
  """Compares the guess with a number. If it matches return True.  If it does not match, print if it is high or low and return False"""
  if guess < number:
    print("Too low.")
    return False
  elif guess > number:
    print("Too high.")
    return False
  else:
    return True
    
  print("")

print(art.logo)

# Generate Random number between 1 and 100
number = random.randint(1,100)

#Print Game Greeting
print("\nWelcome to the Number Guessing Game!")
print("I’m thinking of a number between 1 and 100.")

#Ask the user to choose a difficulty, repeat until valid
valid_difficulty = False
while not valid_difficulty:
  difficulty = input("Choose a difficulty.  Type ‘easy’ or ‘hard: ").lower()
  if difficulty == 'easy':
    tries_left = 10
    valid_difficulty = True
  elif difficulty == 'hard':
    tries_left = 5
    valid_difficulty = True
  else:
    print("That is an invalid response.")

#Repeat prompting for guesses and valididating until
#1 - Guess was correct
#2 - Run out of tries
result_guessed = False
while not result_guessed and tries_left > 0:
  print(f"You have {tries_left} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  response_correct = validate_guess(guess, number)
  if response_correct:
    print(f"\nYou got it! The answer was {number}.")
    result_guessed = True
  else:
    # Response was not correct.  If they have a guess
    # remaining, prompt to guess again.  Decriment the
    # number of tries
    if tries_left > 1:
      print("Guess Again.\n")
    tries_left -= 1
#If the user runs out of guesses, print a message
#and tell them what the number was.
if not result_guessed and tries_left == 0:
    print("\nYou’ve run out of guesses, you lose.")
    print(f"The number was {number}")