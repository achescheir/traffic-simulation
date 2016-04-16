from numpy_traffic import *

def test_find_if_cars_too_close():
    positions = np.array([0, 10, 30])
    speeds = np.array([6, 5, 8])
    lengths = np.array([5, 5, 5])
    loop_length = 100
    check_cars = find_cars_too_close(positions, speeds, lengths, loop_length)
    assert np.array_equal(check_cars, [1, None, None])

def test_handle_cars_too_close():
    positions = np.array([0, 10, 30])
    speeds = np.array([6, 5, 8])
    target_speeds = np.ones(3) * 33
    lengths = np.array([5, 5, 5])
    has_changed = np.zeros(3)
    loop_length = 100
    result_speed, result_has_changed = handle_too_close(positions, lengths, speeds, target_speeds, loop_length, has_changed)
    print(result_speed)
    assert np.array_equal(result_speed, np.array([5, 5, 8]))
    assert np.array_equal(result_has_changed, np.array([True, False, False]))
