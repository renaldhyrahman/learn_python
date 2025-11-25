from .car import Car


class CarControl:
    def __init__(self, data: object):
        self.data = data
        self.populate()

    def populate(self):
        while len(self.data.cars) < self.data.max_car:
            self.data.cars.append(Car(self.data))

    def cars_mov(self):
        # Set padding 2 times of unit's size
        padding = 2 * self.data.screen.size.UNIT
        max_x = self.data.screen.MAX_X + padding
        for i, car in enumerate(self.data.cars):
            car.goto(car.xcor() - self.data.velocity_car, car.ycor())
            if car.xcor() < -max_x:
                del self.data.cars[i]
                self.populate()
