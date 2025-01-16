from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
MSG_FONT = ("Fira Code", 40, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white") 
        self.penup()
        self.player_score = 0
        self.opponent_score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.teleport(-100, 200)
        self.write(f"{self.opponent_score}", align = ALIGNMENT, font=FONT )
        self.teleport(100, 200)
        self.write(f"{self.player_score}", align = ALIGNMENT, font=FONT )
        
    def opponent_point(self):
        self.opponent_score += 1
        print(self.opponent_score)
        self.update_score()
        self.scores_point("Left")

    def player_point(self):
        self.player_score += 1
        print(self.player_score)
        self.update_score()
        self.scores_point("Right")

    # doesnt work
    # def scores_point(self, player):
    #     msg = Turtle()
    #     msg.ht()
    #     msg.color("white")
    #     msg.home()
    #     msg.write(f"{player} scores a point", align=ALIGNMENT, font=MSG_FONT )
    #     time.sleep(1)
    #     # msg.clear()