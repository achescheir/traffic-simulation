from traffic_simulation import *
from unittest import mock
from nose.tools import raises

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

def test_road_empty_constructor():
    b = Road()

def test_road_constructor_has_length():
    b = Road(length = 1000)
    assert b.length == 1000

def test_road_adds_a_car():
    b = Road()
    a = Car()
    b.add_car(a)
    assert b.cars == [a]

def test_add_cars_in_order():
    b = Road()
    a = Car(location = 500)
    c = Car(location = 505)
    b.add_car(a)
    b.add_car(c)
    assert b.cars == [a,c]

@raises(ValueError)
def test_add_car_does_not_allow_same_location():
    b = Road()
    a = Car(location = 500)
    c = Car(location = 500)
    b.add_car(a)
    b.add_car(c)

@raises(ValueError)
def test_add_car_does_not_allow_collision():
    b = Road()
    a = Car(location = 500)
    c = Car(location = 501)
    b.add_car(a)
    b.add_car(c)

@raises(ValueError)
def test_add_car_at_0_tests_at_end():
    b = Road()
    a = Car(location = 999)
    c = Car(location = 0)
    b.add_car(a)
    b.add_car(c)

@raises(ValueError)
def test_add_car_does_not_allow_car_off_end_road():
    b = Road()
    a = Car(location = 1000)
    b.add_car(a)

@raises(ValueError)
def test_add_car_does_not_allow_car_off_start_road():
    b = Road()
    a = Car(location = -10)
    b.add_car(a)

def test_getting_distance_of_cars_from_eachother():
    b = Road()
    a = Car(location = 200)
    c = Car(location = 10)
    assert b.get_distance(c, a) == 185
    assert b.get_distance(a, c) == 805


@raises(ValueError)
def test_get_distance_of_overlapping_cars():
    b = Road()
    a = Car(location = 0)
    c = Car(location = 2)
    b.get_distance(a,c)
