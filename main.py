from turtle import Screen, colormode
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

colormode(255)
# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("The Ping Pong Game")
screen.listen()
screen.tracer(0)


paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.score_increase_left()

    # Detect Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score_increase_right()


screen.exitonclick()
