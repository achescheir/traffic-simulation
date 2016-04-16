import numpy as np
import matplotlib.pyplot as plt

def get_next_positions(positions, speeds, loop_length):
    positions = np.add(positions, speeds) % loop_length
    # print(positions, speeds, loop_length)
    return positions

def handle_collisions(positions, speeds, loop_length, has_changed):
    will_collide = check_for_collisions(positions, speeds, loop_length)
    if np.any(will_collide):
        speeds = np.multiply(speeds, np.logical_not(will_collide))
        print("COLLISION")
        print(will_collide, "will_collide")
        print(speeds,"speeds")
        return speeds, will_collide
    return speeds, has_changed

def handle_speeding_up(speeds, target_speeds, has_changed):
    should_speed_up = speeds < target_speeds
    will_speed_up = np.logical_and(np.logical_not(has_changed), should_speed_up)
    print(has_changed, "has_changed")
    accelerate = will_speed_up * 2
    speeds = speeds + accelerate
    has_changed = has_changed + will_speed_up
    return speeds, has_changed

def sim_tick(positions, speeds, target_speeds, loop_length):
    has_changed = np.zeros(len(positions))
    speeds, has_changed = handle_collisions(positions,speeds,loop_length, has_changed)
    speeds, has_changed = handle_speeding_up(speeds, target_speeds, has_changed)
    print(speeds, "speeds")
    print(has_changed, "has_changed")
    return  speeds, get_next_positions(positions, speeds, loop_length)
        # if will thenstop
        # else if random breaking break
        #else if too close
            #if rear is faster match speeds
            #if rears is slower accelerate
        #else if too slow speed up

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
    positions = np.linspace(0,750,25)#np.array([0, 994])
    speeds = np.array([2, 6])
    target_speed = np.array([33, 33])
    loop_length = 1000
    sim_length= 60
    history = np.zeros((sim_length+1,loop_length))
    snapshot = np.zeros(loop_length)
    for x in positions:
        snapshot[int(x)] = 1
    history[0]= snapshot
    for tick_num in range(sim_length):
        speeds, positions = sim_tick(positions, speeds, target_speed, loop_length)
        snapshot = np.zeros(loop_length)
        for x in positions:
            snapshot[x] = 1
        history[tick_num+1]= snapshot
    plt.matshow(history)
    plt.show()

if __name__ == '__main__':
    main()
