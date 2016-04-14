from traffic_simulation import *
from unittest import mock

def test_car_empty_constructor():
    a = Car()

def test_car_constructor_makes_car():
    a = Car(length = 5, target_speed = 33.3, location = 0, initial_speed = 0, break_chance = 0.1, acceleration = 2)
    assert a.length == 5
    assert a.target_speed == 33.3
    assert a.location == 0
    assert a.initial_speed == 0
    assert a.break_chance == 0.1
    assert a.acceleration == 2

def test_car_speeding_up():
    a = Car()
    a.speed_up()
    assert a.speed == 2

def test_car_breaking():
    a = Car()
    a.speed = 10
    a.breaking()
    assert a.speed == 8

def test_car_should_speed_up_alone():
    a = Car()
    a.speed = 20
    assert a.should_speed_up()

@mock.patch("random.random")
def test_simulate_second(mock_random):
    mock_random.return_value = 1
    a = Car()
    a.sim_tick()
    assert a.location == 2
    assert a.speed == 2
