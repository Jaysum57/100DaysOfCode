from turtle import Turtle


class Navigator(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()

    def move(self, x_cor, y_cor):
        print(x_cor)
        print(y_cor)
        self.teleport(x_cor,y_cor)

    def write_state(self,state):
        print(state)
        self.write(state,align="center", font=("Arial", 10, "normal"))