import numpy as np

def get_next_positions(positions, speeds, loop_length):
    positions = np.add(positions, speeds) % loop_length
    # print(positions, speeds, loop_length)
    return positions

def sim_tick(positions, speeds, target_speed, loop_length):
    has_changed = np.zeros(len(positions))
    will_collide = check_for_collisions(positions, speeds, loop_length)
    if np.any(will_collide):
        speeds = np.multiply(speeds, np.logical_not(will_collide))
        has_changed = will_collide
        print("COLLISION")
    should_speed_up = speeds < target_speed
    will_speed_up = np.logical_and(np.logical_not(has_changed), should_speed_up)
    print(has_changed, "has_changed")
    accelerate = will_speed_up * 2
    speeds = speeds + accelerate
    has_changed = has_changed + will_speed_up
    print(speeds, "speeds")
    print(has_changed, "has_changed")
    return  speeds, get_next_positions(positions, speeds, loop_length)

def difference_of_speeds(speeds):
    a, b = np.meshgrid(speeds, speeds)
    return((b-a))

def distance_between_cars(positions, loop_length):
    a, b = np.meshgrid(positions, positions)
    return((a - b) % loop_length)

def check_for_collisions(positions, speeds, loop_length):
    print(positions,"Current_positions\n")
    current_distances  = distance_between_cars(positions,loop_length)
    print(current_distances,"current_distances\n")
    current_difference_of_speeds = difference_of_speeds(speeds)
    print(current_difference_of_speeds,"current_difference_of_speeds\n")
    return np.any(current_distances < current_difference_of_speeds, axis = 1)

def main():
    positions = np.array([0, 994])
    speeds = np.array([2, 6])
    target_speed = np.array([33, 33])
    loop_length = 1000
    for _ in range(8):
        speeds, positions = sim_tick(positions, speeds, target_speed, loop_length)


if __name__ == '__main__':
    main()
