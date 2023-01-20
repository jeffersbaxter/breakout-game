import random
from turtle import Turtle

COLORS = ["red", "yellow", "green", "blue", "purple"]


class BrickManager(Turtle):

    def __init__(self):
        self.all_bricks = []

    def create_brick(self):
        for row in range(4):
            for i in range(10):
                new_brick = Turtle("square")
                new_brick.shapesize(stretch_len=3.5, stretch_wid=1)
                new_brick.penup()
                new_brick.color(random.choice(COLORS))
                new_brick.goto(-340 + (i * 75), 200 - (row * 25))
                self.all_bricks.append(new_brick)

    def delete_brick(self, brick):
        brick.hideturtle()
        self.all_bricks.remove(brick)
