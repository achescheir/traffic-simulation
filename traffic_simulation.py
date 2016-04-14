import math

class Car:
    def __init__(self, length=5, target_speed=100/3, location=0, initial_speed=0, break_chance=0.1, acceleration=2):
        self.length = length
        self.target_speed = target_speed
        self.location = location
        self.initial_speed = initial_speed
        self.break_chance = break_chance
        self.acceleration = acceleration
        self.speed = self.initial_speed

    def speed_up(self):
        self.speed += self.acceleration

    def breaking(self):
        self.speed -= self.acceleration

    def should_speed_up(self):
        return self.speed < self.target_speed

    def sim_tick(self):
        if self.should_speed_up():
            self.speed_up()
        self.location += self.speed

class Road:
    def __init__(self, length=1000):
        self.length = length
        self.cars = []

    def add_car(self, car):
        if car.location >= self.length or car.location < 0:
            raise ValueError

        if len(self.cars) <= 0:
            self.cars.append(car)
            return
        for each_car in self.cars[:]:
            try:
                self.get_distance(each_car,car)
            except ValueError as e:
                raise e
                
        self.cars.append(car)
        self.cars.sort(key = lambda x : x.location)


    def get_distance(self, back_car, front_car):
        shift = back_car.location - back_car.length
        back_of_back_car = 0
        front_of_back_car = back_car.length

        back_of_front_car = front_car.location-front_car.length-shift
        if back_of_front_car <0:
            back_of_front_car = self.length+back_of_front_car

        front_of_front_car = front_car.location-shift
        if front_of_front_car <0:
            front_of_front_car = self.length + front_of_front_car

        if front_of_front_car <= front_of_back_car or back_of_front_car < front_of_back_car:
            raise ValueError
        else:
            return back_of_front_car - front_of_back_car
