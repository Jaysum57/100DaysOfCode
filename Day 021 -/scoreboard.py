from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Fira Code", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.ht()
        self.speed("fastest")
        self.goto(0,270)
        self.color("white")
        self.update_score()
    
    def update_score(self):
        self.write(f"Score: {self.score}", 
                   align=ALIGNMENT, 
                   font=FONT )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"GAMEOVER", 
            align=ALIGNMENT, 
            font=FONT )
