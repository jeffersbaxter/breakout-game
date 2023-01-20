from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(pos)

    def go_left(self):
        negative_x = self.xcor() - 20
        self.goto(negative_x, self.ycor())

    def go_right(self):
        positive_x = self.xcor() + 20
        self.goto(positive_x, self.ycor())
