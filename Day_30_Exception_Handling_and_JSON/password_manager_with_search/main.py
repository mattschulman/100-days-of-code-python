from tkinter import *
from tkinter import messagebox
from  random import randint, choice, shuffle
import pyperclip
import json

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

# ---------------------------- SEARCH FOR WEBSITE -------------------------- #
def find_password():
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(message="No Data File Found.")
    website = website_entry.get()
    if website not in data:
        messagebox.showwarning(message="No Details for the Website Exists.")
    else:
        username = data[website]["username"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = user_entry.get()
    pw = pw_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": pw
        }
    }

    if len(username) == 0 or len(pw) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                try:
                    data = json.load(data_file)
                except json.JSONDecodeError:
                    #File existed by didn't have JSON data in it
                    data = {}

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file,indent=4) 
        #Read old data
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #write updated data to file
                json.dump(data, data_file, indent=4)
        finally:
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
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1,column=2)

pw_button = Button(text="Generate Password",command=generate_password)
pw_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2)

#Entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

user_entry = Entry(width=38)
user_entry.insert(0,"user@email.com")
user_entry.grid(row=2, column=1, columnspan=2)

pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)

window.mainloop()