rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choices = ["rock", "paper", "scissors"]

your_choice = input('Choose "rock", "paper", or "scissors" -> ')
my_choice = random.choice(choices)

if your_choice == "rock":
  print("Your Choice:")
  print(rock)
  print("")
  if my_choice == "paper":
    print("My Choice:")
    print(paper)
    print("")
    print("I WIN!!")
  elif my_choice == "scissors":
    print("My Choice:")
    print(scissors)
    print("")
    print("You WIN!!")
  else:
    print("My Choice:")
    print(rock)
    print("")
    print("TIE!!")
elif your_choice == "paper":
  print("Your Choice:")
  print(paper)
  print("")
  if my_choice == "rock":
    print("My Choice:")
    print(rock)
    print("")
    print("You WIN!!")
  elif my_choice == "scissors":
    print("My Choice:")
    print(scissors)
    print("")
    print("I WIN!!")
  else:
    print("My Choice:")
    print(paper)
    print("")
    print("TIE!!")
elif your_choice == "scissors":
  print("Your Choice:")
  print(scissors)
  print("")
  if my_choice == "rock":
    print("My Choice:")
    print(rock)
    print("")
    print("I WIN!!")
  elif my_choice == "paper":
    print("My Choice:")
    print(paper)
    print("")
    print("You WIN!!")
  else:
    print("My Choice:")
    print(scissors)
    print("")
    print("TIE!!")
else:
  print('Invalid Choice: You must enter "rock", "paper", or "scissors". Try again.')