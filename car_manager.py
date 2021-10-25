from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
car_size = [2, 3, 4]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()

        self.garage = []
        self.x_pos = 380


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            y_pos = random.randint(-250,250)
            new_car.penup()
            new_car.color(COLORS[random.randint(0,5)])
            new_car.shapesize(stretch_wid=1, stretch_len= car_size[random.randint(0,2)])
            new_car.goto(self.x_pos, y_pos)
            self.garage.append(new_car)

    def move(self):
        for cars in self.garage:
            cars.backward(MOVE_INCREMENT)


