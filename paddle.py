from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__(self)
        self.paddle()
        self.segment = Turtle()
        self.p = paddle_position

    def paddle(self):
        self.segment.shape("square")
        self.segment.color("white")
        self.segment.turtlesize(stretch_wid=5, stretch_len=1)
        self.segment.penup()
        self.segment.goto(self.p)

    def go_up(self):
        new_y = self.segment.ycor() + 20
        self.segment.goto(self.segment.xcor(), new_y)

    def go_down(self):
        new_y = self.segment.ycor() - 20
        self.segment.goto(self.segment.xcor(), new_y)
