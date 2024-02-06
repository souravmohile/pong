from turtle import Screen, Turtle
from pad import Pad
from ball import Ball
from score import Scoreboard
import time

turtle = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)

score = Scoreboard()

r_pad = Pad((350, 0))
l_pad = Pad((-350, 0))

screen.listen()
screen.onkey(l_pad.up, "w")
screen.onkey(l_pad.down, "s")
screen.onkey(r_pad.up, "Up")
screen.onkey(r_pad.down, "Down")

turtle.penup()
turtle.hideturtle()
turtle.color("white")
turtle.pensize(5)
turtle.goto(0, 280)
turtle.right(90)
for _ in range(14):
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)

ball = Ball()

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()
