from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

def flip_card():
    # Set the background to the green image, set the title to "English" with white text, and print the english word.
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def next_card():
    #Cancel the timer if there is one (if you keep hitting "known"), get a random word from the dict, set the title to "French"
    # and text color to black, the background to the front image, print the French word, and set a 3 second (3000msec) timer.
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(word_dict)
    #print(random_word)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def known_word():
    #If a word is marked as "Known", remove it from the dictionary, then convert the dictionary to a Pandas DataFrame and
    #save as a CSV file and call the next_card() funtion to display a new card.
    word_dict.remove(current_card)
    #print(len(word_dict))
    data_to_save = pandas.DataFrame(word_dict)
    data_to_save.to_csv("data/words_to_learn.csv", index=False)
    next_card()


#---------------UI----------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#images
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")

#canvas
canvas = Canvas(width=800, height=526) 
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", fill="black",font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#buttons
dont_know_button = Button(image=wrong_image, highlightthickness=0,command=next_card)
dont_know_button.grid(row=1,column=0)

know_button = Button(image=right_image, highlightthickness=0,command=known_word)
know_button.grid(row=1,column=1)

#---------Main Code----------------------#

#Try to open the CSV file of words still to learn.  If it is not found, then open the CSV with the full list of words. 
#Convert to a Pandas DataFrame
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

#Convert the DataFrame to a Python dictionary, oriented by records so that each entry is <french_word>:<english_word>
word_dict = data.to_dict(orient="records")
#print (word_dict)

#Start by picking a random card
next_card()
window.mainloop()