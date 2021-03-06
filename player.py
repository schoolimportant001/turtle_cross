from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.speed("fastest")
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.speed("fastest")
        self.backward(MOVE_DISTANCE)

    def reset_location(self):
        self.goto(STARTING_POSITION)