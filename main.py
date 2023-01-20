import time
from turtle import Screen

from ball import Ball
from brick_manager import BrickManager
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=750, height=464)
screen.title("Breakout")
screen.tracer(0)

brick_manager = BrickManager()
ball = Ball()
paddle = Paddle((0, -175))
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

brick_manager.create_brick()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    for brick in brick_manager.all_bricks:
        if brick.distance(ball) < 30:
            brick_manager.delete_brick(brick)
            ball.bounce_y()

    if ball.xcor() > 355 or ball.xcor() < -355:
        ball.bounce_x()

    if ball.distance(paddle) < 50 and ball.ycor() < -145:
        ball.bounce_y()

    if ball.ycor() < -192:
        game_is_on = False

screen.exitonclick()
