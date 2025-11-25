from .car import Car


class CarControl:
    def __init__(self, config: object):
        self.config = config
        self.cars = []
        self.max_car = 20
        self.populate()

    def populate(self):
        while len(self.cars) < self.max_car:
            self.cars.append(Car(self.config))

    def cars_mov(self):
        padding = self.config.size.UNIT * 2
        max_x = self.config.MAX_X + padding
        for i, car in enumerate(self.cars):
            car.fd(self.config.size.UNIT)
            if car.xcor() < -max_x:
                del self.cars[i]
                self.populate()
