from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.teleport(-250,220)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: \n{self.level}", align = "left", font=FONT )

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.home()
        self.write(f"GAME OVER.", align = "center", font=FONT )