from turtle import Turtle



class Level(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()   
        self.goto(-20, 270)
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write("Level: " + str(self.level), align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("Courier", 40, "normal"))