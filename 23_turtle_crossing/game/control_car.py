from .car import Car


class CarControl:
    def __init__(self, data: object):
        self.data = data
        self.populate()

    def populate(self):
        while len(self.data.cars) < self.data.max_car:
            self.data.cars.append(Car(self.data))

    def cars_mov(self):
        # Set padding 2 times of unit size
        size_unit = self.data.screen.size.UNIT
        padding = 2 * size_unit
        max_x = self.data.screen.MAX_X + padding
        for i, car in enumerate(self.data.cars):
            car.goto(car.xcor() - size_unit, car.ycor())
            # car.fd(self.data.screen.size.UNIT)
            if car.xcor() < -max_x:
                del self.data.cars[i]
                self.populate()
