from tkinter import *

def miles_to_km():
    miles = float(input.get())
    #print(miles)
    km = round(miles * 1.609)
    #print(km)
    result_label.config(text=f"{km}")


FONT = ("Arial",12,"normal")

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

input = Entry(width=7)
input.insert(END, string="0")
input.grid(row=0, column=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

equals_label = Label(text="is equal to", font=FONT)
equals_label.grid(row=1, column=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

result_label = Label(text="0", font=FONT)
result_label.grid(row=1, column=1)

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()