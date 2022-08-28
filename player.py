from turtle import*

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x_cor, y_cor)
        self.setheading(90)


    def move(self):
        y=self.ycor()+30
        self.goto(self.xcor(), y)
