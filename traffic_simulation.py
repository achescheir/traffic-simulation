
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
