from turtle import Turtle
import random

back_speed = 5
starting_speed = 5

class Car():
    
    def __init__(self):
        self.cars = []
        self.reserve_car = []
        self.car_speed = starting_speed

        
    def add_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:

            if self.reserve_car:
                new_car = self.reserve_car.pop()
            else:
                new_car = Turtle("square")
                new_car.color(self.random_color())
                new_car.shapesize(stretch_len=2, stretch_wid=1) 
                new_car.penup()
            
            new_car.goto(300, random.randint(-230, 230))
            self.cars.append(new_car)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def move(self):
        for c in self.cars:
            c.goto(c.xcor() - self.car_speed, c.ycor())
            if c.xcor() < -320:
                self.cars.remove(c)
                self.reserve_car.append(c)

    def increase_back_movement(self):
        self.car_speed += back_speed

