from vectorized_traffic_sim import *
import numpy as np

def test_wrap_positions():
    start_positions = np.array([0,125,250,375])
    wrapped_positions = wrap(start_positions,300)
    assert np.array_equal(wrapped_positions, np.array([0,125,250,75]))

def test_move():
    start_positions = np.array([0,50,100,150,200,250])
    speeds = np.array([100,110,120,130,140,145])
    assert np.array_equal(move(start_positions,speeds,300),np.array([100,160,220,280,40,95]))

def test_get_rears():
    start_positions = np.array([0,50,100,150,200,250])
    lengths = np.array([10,5,5,10,5,5])
    road_length = 300
    assert np.array_equal(get_rears(start_positions, lengths,road_length),np.array([290,45,95,140,195,245]))

def test_get_distances():
    fronts = np.array([0,10,20,50])
    rears = np.array([55, 5,18,40])
    loop_length = 60
    assert np.array_equal(get_distances(fronts, rears, loop_length),np.array([[55,5,18,40],
                                                                              [45,55,8,30],
                                                                              [35,45,58,20],
                                                                              [5,15,28,50]]))

def test_find_collisions_OK():
    fronts = np.array([0,10,20,50])
    lengths = np.array([5,5,5,5])
    loop_length = 60
    rears = get_rears(fronts,lengths,loop_length)
    assert np.array_equal(find_collisions(rears, fronts,lengths, loop_length),[False, False, False, False])

def test_find_collisions_touch():
    fronts = np.array([0,10,20,50])
    lengths = np.array([10,5,5,5])
    loop_length = 60
    rears = get_rears(fronts,lengths,loop_length)
    assert np.array_equal(find_collisions(rears, fronts,lengths, loop_length),[False, False, False, True])

def test_find_collisions_overlap():
    fronts = np.array([0,10,20,50])
    lengths = np.array([10,12,5,5])
    loop_length = 60
    rears = get_rears(fronts,lengths,loop_length)
    assert np.array_equal(find_collisions(rears, fronts,lengths, loop_length),[True, False, False, True])

def test_are_any_collisions_OK():
    fronts = np.array([0,10,20,50])
    lengths = np.array([5,5,5,5])
    loop_length = 60
    assert np.array_equal(are_any_collisions(fronts,lengths, loop_length),False)

def test_are_any_collisions_touch():
    fronts = np.array([0,10,20,50])
    lengths = np.array([10,5,5,5])
    loop_length = 60
    assert np.array_equal(are_any_collisions(fronts,lengths, loop_length),True)

def test_are_any_collisions_overlap():
    fronts = np.array([0,10,20,50])
    lengths = np.array([12,5,5,5])
    loop_length = 60
    assert np.array_equal(are_any_collisions(fronts,lengths, loop_length),True)

def test_get_difference_of_speeds():
    speeds = np.array([10,15,10])
    assert np.array_equal(get_difference_of_speeds(speeds),[[0,5,0],[-5,0,-5],[0,5,0]])

def test_should_stop():
    fronts = np.array([0,10,20,50])
    lengths = np.array([5,5,5,5])
    speeds = [10,2,1,1]
    loop_length = 60
    assert np.array_equal(should_stop(fronts, lengths, speeds, loop_length),[True, False, False, False])

def test_are_too_close():
    fronts = np.array([0,10,20,50])
    lengths = np.array([5,5,5,5])
    speeds = [10,2,1,1]
    loop_length = 60
    are_too_close(fronts, lengths, speeds, loop_length)
    assert np.array_equal(are_too_close(fronts, lengths, speeds, loop_length),[True, False, False, False])

def test_are_too_slow():
    speeds = np.array([0,20,50,45])
    target_speeds = np.array([33, 33, 33, 45])
    assert np.array_equal(are_too_slow(speeds,target_speeds),[True, True, False, False])

def test_speed_up():
    speeds= [0, 10, 20, 40]
    should_speed_up=[True, False, True, True]
    target_speeds=[33,33,21,33]
    accelerations = [2,2,2,2]
    assert np.array_equal(speed_up(speeds,should_speed_up,target_speeds,accelerations),[2,10,21,33])
# def test_change_speed_speed_up():
#     start_positions = np.array([0,50,100,150,200,250])
#     start_speeds = 25 * np.ones(6)
#     target_speeds = (100/3) * np.ones(6)
#     assert np.array_equal(should_speed_up(start_positions,start_speeds,target_speeds),np.ones(6))
