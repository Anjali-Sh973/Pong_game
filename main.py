from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
