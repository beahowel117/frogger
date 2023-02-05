from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frogger")
screen.tracer(0)

frog = Player()

screen.listen()
screen.onkeypress(frog.cross_street, "Up")

game_is_on = True
while game_is_on:
    #tracer is off, instead game (everything in loop) will be refreshed every .1s
    time.sleep(0.1)
    screen.update()

screen.exitonclick()

