from numpy_traffic import *

def test_find_if_cars_too_close():
    positions = np.array([0, 10, 30])
    speeds = np.array([6, 5, 8])
    lengths = np.array([5, 5, 5])
    loop_length = 100
    check_cars = find_cars_too_close(positions, speeds, lengths, loop_length)
    assert np.array_equal(check_cars, [1, None, None])
