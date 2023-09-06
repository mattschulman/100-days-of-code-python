import random
import art
import os

def clear():
  if os.name == 'nt':
    _ = os.system('cls')
  else: 
    _ = os.system('clear')
    
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  score = sum(cards)
  if score == 21:
    return 0
  elif score > 21:
    index = 0
    for card in cards:
      if cards[index] == 11:
        cards[index] = 1
        score = sum(cards)
        if score <= 21:
          break
      index += 1
    return score
  else:
    return score

def compare(user_score, computer_score):
  if user_score > 21:
    print("You have busted.  You lose.")
  elif computer_score > 21:
    print("Computer Busted.  You win!")
  elif user_score > computer_score:
    print("You win!")
  elif computer_score > user_score:
    print("Computer wins!")
  else:
    print("Game results in a tie.")


keep_playing = True
print(art.logo)
while keep_playing:
  user_cards = []
  computer_cards = []
  num_cards = 0   
  while num_cards < 2:
    user_card_dealt = deal_card()
    computer_card_dealt = deal_card()
    user_cards.append(user_card_dealt)
    computer_cards.append(computer_card_dealt)
    num_cards +=1
  
  user_score = calculate_score(user_cards)  
  computer_score = calculate_score(computer_cards)
  
  print(f"Your Cards: {user_cards}, current score: {user_score}")
  print(f"Computer's first card: {computer_cards[0]}")
  
  
  if user_score == 0 :
    print("You have Blackjack!  You Win!")
    #exit(0)
  elif computer_score == 0:
    print("The Computer has Blackjack!  The Computer Wins")
    #exit(0)
  elif user_score > 21:
    print("You have busted.  You lose.")
  else:
    keep_drawing = True
    while keep_drawing:
      draw_another_card = input("Type 'y' to get another card, or 'n' to stay. ")
      if draw_another_card == 'y':
        user_cards.append(deal_card())
        print(user_cards)
        user_score = calculate_score(user_cards)
        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score > 21:        
          keep_drawing = False
      else:
        keep_drawing = False
    print(f"Your Cards: {user_cards}, current score: {user_score}")    
    if user_score <=21:
      while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        if computer_score == 21:
          break
        elif computer_score > 21:
          break
      print(f"Computer Cards: {computer_cards}. Computer Score: {computer_score}")
    compare(user_score, computer_score)

  result = input("Play another game? 'y' or 'n': ")
  if result == 'y':
    keep_playing = True
    clear()
    print(art.logo)
  else:
    keep_playing = False

