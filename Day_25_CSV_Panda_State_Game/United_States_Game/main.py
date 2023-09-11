import turtle
import pandas

#Read in the CSV into a panda DataFrame and extract the state names to a list
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

# Create the screen, and set the shape to be the blank_states_img.gif image.
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#This is the code used to get the coordinates of each state in the image.  These coordinates
#were put in the csv file.
#
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state?").title()
    if answer_state == 'Exit':
        break
    #If the answer matches a state in the panda, write the answer on the screen in the correct spot.
    #if states_data.state.str.contains(answer_state).any():
    if answer_state in states:
        if answer_state not in guessed_states:
            #Create the turtle, hide it, and do penup() so that lines aren't drawn
            state = turtle.Turtle()
            state.hideturtle()
            state.penup()
            #Get the row for the state in the panda
            state_data = data[data.state == answer_state]
            #Get the x and y coordinates for the state
            x_cor = state_data.x.item()
            y_cor = state_data.y.item()
            #write the state answer to screen at the coordinates.
            state.goto(x_cor, y_cor)
            state.write(answer_state, align="center", font=('Arial', 8, 'bold'))
            #Add the answer to the guessed_states list.
            guessed_states.append(answer_state)



#Generate a list of results that show if the state was guessed
state_results = []
for state in states:
    Guessed = False
    for guess in guessed_states:
        if guess == state:
            Guessed = True
    state_results.append(Guessed)

#Save the list of states and the results into a dictionary
results = {
    "States": states,
    "Guessed": state_results
}


#Use panda to create a CSV of the results
output = pandas.DataFrame(results)
output.to_csv("states_game_results.csv")

#screen.exitonclick()