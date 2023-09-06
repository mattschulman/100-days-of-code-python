import random
#from replit import clear
import os
import art
import game_data

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else: 
        _ = os.system('clear')

def interface(score,answer,a,b):
  """ This function generates the game interface, asking the user to guess which has the higher follower count.  It compares the guess to the correct answer and returns True or False depending of the guess was correct or not. 
  INPUTS: the current score, the answer, and the a and b dictionaries.
  OUTPUTS: True or False"""
  print(art.logo)
  if score > 0:
    print(f"You’re right! Current Score: {score}")
  print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}')
  print(art.vs)
  print(f'Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}')
  valid_guess = False
  while not valid_guess:
    guess = input("Who has more followers? Type ‘A’ or ‘B'").lower()
    if guess == 'a' or guess == 'b':
      valid_guess = True
    else:
      print("Only 'A' or 'B' are valid inputs.")
  if guess == 'a':
    guess_count = a["follower_count"]
  else:
    guess_count = b["follower_count"]
  #print(guess_count)
  #print(answer)
  if guess_count == answer:
    return True
  else:
    return False
        
def play_game(score):
  #Create empty dictionaries for a and b contestents
  a = {}
  b = {}
  a = random.choice(game_data.data)
  b = random.choice(game_data.data)
  #print(a)
  #print(b)
  # Make sure that a and b are different.  If they
  # are the same, rechoose B until they are different
  different = False
  while not different: 
    if a["name"] == b["name"]:
      #print("Dictionaries are the same. Re-choosing B")
      b = random.choice(game_data.data)
    else:
      #print("Dictionaries are different. Continuing")
      different = True
  #Compare the follower_count values.  Set answer to the higher number.
  if a["follower_count"] > b["follower_count"]:
    #print("A is higher than B")
    answer = a["follower_count"]
  else:
    #print("B is higher than A")
    answer = b["follower_count"]
  #print(f"Highest follower count - {answer}")
  #Call the interface function to display the contestents and to prompt the user to guess between them.  It will return True or False depending on if the guess was correct.
  result = interface(score=score,
                      answer=answer,
                      a=a,
                      b=b)
  return result
    

#set the scrore to 0 to start
score = 0
keep_playing=True
result = play_game(score)
while keep_playing:
  if result:
    score +=1
    clear()
    result = play_game(score)
  else:
    print(f"Sorry, that’s wrong.  Final Score: {score}")
    keep_playing = False