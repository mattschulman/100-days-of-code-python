from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
#WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
#Create a global variable called timer to hold the window.after() object in countdown().  It is needed to be 
#able to cancel it in timer_reset().
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps+=1
    #print(f"Iteration: {reps}")

    # if it's the 1st/3rd/5th/7th rep, call countdown with work_sec
    # if it's the 8th rep, call countdown with long_break_sec
    # if it's the 2nd/4th/6th rep, call countdown with short_break_sec
    if reps % 8 == 0:
        #print(f"Counter {long_break_sec} seconds")
        title_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        #print(f"Counter {short_break_sec} seconds")
        title_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        #print(f"Counter {work_sec} seconds")
        title_label.config(text="Work", fg=GREEN)
        countdown(work_sec)

        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    min = count // 60
    sec = count % 60
    global reps
    #Set the canvas element for the timer to the count
    canvas.itemconfig(timer_text, text=f"{min:02d}:{sec:02d}")
    # Use the tkinter after() function to wait 1000 msec and then call itself and decrement the count by 1 and restart 
    # the timer when count is= 0
    if count > 0:
        #Reference the global timer variable and set the window.after() object to it so it can be cancelled by 
        #reset_timer()
        global timer
        timer = window.after(1000, countdown, count-1) 
    else:
        start_timer()
        if reps % 2 == 0:
            checks=""
            for _ in range(math.floor(reps/2)):
                checks += "✓" 
            checkmarks_label.config(text=checks)
        # if reps == 8:
        #     reps = 0


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

#Create a canvas for the tomato image.  Canvases allow widgets to be placed on top of them.
#highlightthickness=0 removes the border around the image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_png)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label=Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
title_label.grid(row=0, column=1)

checkmarks_label = Label(bg=YELLOW, fg=GREEN)
checkmarks_label.grid(row=3, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()