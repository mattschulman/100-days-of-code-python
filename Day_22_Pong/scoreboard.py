from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ('Courier', 80, 'normal')
GAME_OVER_FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100,200)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=SCORE_FONT)
        self.goto(100,200)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=SCORE_FONT)

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()
    
    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        if self.right_score > self.left_score:
            self.write("GAME OVER - Right Side Wins!", align=ALIGNMENT, font=GAME_OVER_FONT)
        else:
            self.write("GAME OVER - Left Side Wins!", align=ALIGNMENT, font=GAME_OVER_FONT)