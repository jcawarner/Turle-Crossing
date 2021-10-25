import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#create objects
player = Player()
score = Scoreboard()
car = CarManager()

screen.onkeypress(player.move, "Up")
screen.listen()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    if car.distance(player) < 20:
        print("squashed")

