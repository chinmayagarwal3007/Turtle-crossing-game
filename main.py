from turtle import Turtle, Screen
from player import Player
from car import Car
from level import Level
import time

screen = Screen()

screen.setup(600, 600)
screen.tracer(0)
screen.title("Crossing Game")
screen.listen()
screen.colormode(255)

player = Player()

game_is_on = True
car = Car()
level = Level()

screen.onkeypress(player.move_fordward, "Up")
screen.onkeyrelease(player.stop, "Up")

def move():
    player.move()
    screen.ontimer(move, 50)

move()



while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_car()
    car.move()

    for c in car.cars:
        if c.distance(player) < 15:
            game_is_on = False

    if (player.ycor() > 250):
        level.update_level()
        player.go_to_starting_pos()
        car.increase_back_movement()

level.game_over()


screen.exitonclick()