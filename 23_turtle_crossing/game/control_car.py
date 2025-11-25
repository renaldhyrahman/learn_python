from .car import Car


class CarControl:
    def __init__(self, data: object):
        self.data = data
        self.populate()

    def populate(self):
        while len(self.data.cars) < self.data.max_car:
            self.data.cars.append(Car(self.data))

    def cars_mov(self):
        # Set offset 4 times of unit's size
        offset = 4 * self.data.screen.size.UNIT
        max_x = self.data.screen.MAX_X + offset
        new_cars = []
        for car in self.data.cars:
            distance = car.direction * self.data.velocity_car
            car.goto(car.xcor() + distance, car.ycor())
            if (car.direction < 0 and car.xcor() < -max_x) or (
                car.direction > 0 and car.xcor() > max_x
            ):
                self.populate()
            else:
                new_cars.append(car)
        self.data.cars = new_cars
