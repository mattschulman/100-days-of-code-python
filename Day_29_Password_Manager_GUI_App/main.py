from tkinter import *
from tkinter import messagebox
from  random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= randint(8,10)
    nr_symbols = randint(2,4)
    nr_numbers = randint(2,4)

    letter_list = [choice(LETTERS) for _ in range(nr_letters)]
    symbol_list = [choice(SYMBOLS) for _ in range(nr_symbols)]
    number_list = [choice(NUMBERS) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)
    password = "".join(password_list)
    #print(f"Your password is: {password}")
    pw_entry.insert(0,password)
    #copy the password to the system clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = user_entry.get()
    pw = pw_entry.get()

    if len(username) == 0 or len(pw) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        #Show the user the info entered and to confirm if they want to save it
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail/Username: {username}"
                            f"\nPassword: {pw}\n Is it OK to save?")
        
        #If the user clicks OK, save the info and clear out the data in the form.
        if is_ok:
            line = f"{website} | {username} | {pw}\n"

            with open("data.txt", "a") as data_file:
                data_file.writelines(line)
            #clear out the entred information and set the focus to the website entry    
            website_entry.delete(0,END)
            pw_entry.delete(0,END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

canvas = Canvas(width=200, height=200)
logo_png=PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_png)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

#Buttons
pw_button = Button(text="Generate Password",command=generate_password)
pw_button.grid(row=3, column=2)

add_button = Button(text="Add", width=38,command=save)
add_button.grid(row=4, column=1, columnspan=2)

#Entries
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

user_entry = Entry(width=40)
user_entry.insert(0,"user@email.com")
user_entry.grid(row=2, column=1, columnspan=2)

pw_entry = Entry(width=22)
pw_entry.grid(row=3, column=1)

window.mainloop()