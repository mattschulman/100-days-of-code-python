import tkinter

def button_clicked():
    #print("I got clicked")
    my_label["text"] = input.get()

#Create window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
#Update the padding around the window.  Use confg and padx= and pady= to change the padding in the x and y axes around the window
window.config(padx=20, pady=20)

#Create label
my_label = tkinter.Label(text="I am a label",font=("Arial",24,"bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text 2")
#pack() places widgets starting at the top and working down.
#Can use the side= parameter to not place at top ("left", "right", or "bottom")
#
#my_label.pack()
#
#place() allows for precise placement of a widget using an x and y value (0,0 is top left of the screen)
#increasing the x value moves to right.  increasing the y value moves it down.
#
#my_label.place(x=0, y=0)
#
#grid() divides the screeen into rows and columns for widget placement (row 0 is top and column 0 is left)
#rows and columns are relative to other widgets using grid.  for the only widget using grid, row 5 and column 6 still
#show up in the top left because no other widgets have a row or column defined.
#Cannoth use grid() and pack() in the same script.  You will error out.
#
my_label.grid(row=0, column=0)
#
#Can also add padding around widgets
#
my_label.config(padx=50, pady=50)

#Button

button = tkinter.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(row=1, column=1)

new_button = tkinter.Button(text="No click me!", command=button_clicked)
new_button.grid(row=0, column=2)


#Entry
input = tkinter.Entry(width=10)
print(input.get())
#input.pack()
input.grid(row=2, column=3)




window.mainloop()