from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frogger")
screen.tracer(0)

frog = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(frog.cross_street, "Up")

game_is_on = True
while game_is_on:
    #tracer is off, instead game (everything in loop) will be refreshed every .1s
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect when a frog collides with a car
    for car in car_manager.all_cars:
        if frog.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect frog successfully crosses
    if frog.is_at_finish_line() == True:
        scoreboard.increase_score()
        frog.go_to_start()
        car_manager.level_up()

screen.exitonclick()

