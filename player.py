from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)
        self.setheading(90)
        self.moving = False
    
    def move_fordward(self):
        self.moving = True

    def go_to_starting_pos(self):
        self.goto(0, -280)

    def stop(self):
        self.moving = False

    def move(self):
        if self.moving:
            self.forward(10)