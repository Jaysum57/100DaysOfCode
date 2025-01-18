from turtle import Turtle



ALIGNMENT = "center"
FONT = ("Fira Code", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.ht()
        self.speed("fastest")
        self.goto(0,270)
        self.color("white")
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", 
                   align=ALIGNMENT, 
                   font=FONT )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
            self.high_score = self.score
            
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write(f"GAMEOVER", 
    #         align=ALIGNMENT, 
    #         font=FONT )
