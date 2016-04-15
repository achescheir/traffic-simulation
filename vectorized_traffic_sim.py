import numpy as np


def wrap(positions, length):
    return positions % length

def move(positions,speeds,length):
    return  wrap(positions + speeds, length)

def get_rears(fronts, lengths, loop_length):
    return wrap(fronts - lengths, loop_length)

def get_distances(behind_elements, ahead_elements, loop_length):
    ahead_grid, behind_grid = np.meshgrid(ahead_elements, behind_elements)
    relative_ends = wrap(ahead_grid - behind_grid, loop_length)
    return relative_ends

def find_collisions(base_lines, ends_of_cars,lengths, loop_length):
    relative_ends = get_distances(base_lines, ends_of_cars, loop_length)
    np.fill_diagonal(relative_ends,loop_length)
    distance_to_end_of_next_car = np.amin(relative_ends, axis = 0)
    distance_to_end_too_short = distance_to_end_of_next_car < lengths
    return distance_to_end_too_short

def are_any_collisions(fronts, lengths, loop_length):
    rears = get_rears(fronts,lengths,loop_length)
    fronts_inside_car = find_collisions(rears , fronts, lengths, loop_length)
    rears_inside_car = find_collisions(rears , rears, lengths, loop_length)
    return any(np.logical_or(fronts_inside_car, rears_inside_car))

def get_difference_of_speeds(speeds):
    aheadspeed_grid, behind_speed_grid = np.meshgrid(speeds,speeds)
    difference_of_speeds = aheadspeed_grid - behind_speed_grid
    return difference_of_speeds

def should_stop(fronts, lengths, speeds, loop_length):
    distances = get_distances(fronts, get_rears(fronts, lengths,loop_length), loop_length)
    difference_of_speeds = get_difference_of_speeds(speeds)
    future_distance = distances + difference_of_speeds
    will_collide = future_distance <= 0
    return np.any(will_collide,axis = 1)

def are_too_close(fronts, lengths, speeds, loop_length):
    distances = get_distances(fronts, get_rears(fronts, lengths,loop_length), loop_length)
    difference_of_speeds = get_difference_of_speeds(speeds)
    future_distance = distances + difference_of_speeds
    speed_grid, _ = np.meshgrid(speeds, speeds)
    will_be_too_close = future_distance <= speed_grid
    cars_that_are_too_close = np.argwhere(will_be_too_close == True)
    # print(cars_that_are_too_close)
    return [[z[1] for z in cars_that_are_too_close if z[0]==a ]for a in range(len(fronts))]

def are_too_slow(speeds, target_speeds):
    return speeds < target_speeds

def speed_up(speeds, should_speed_up, target_speeds, accelerations):
    temporary_speeds = speeds + np.multiply(should_speed_up, accelerations)
    return np.minimum(temporary_speeds,target_speeds)

def slow_down(speeds, should_slow_down,  accelerations):
    temporary_speeds = speeds - np.multiply(should_speed_up, accelerations)
    return np.maximum(np.zeros(len(target_speeds)),target_speeds)

def stop_vehicles(speed,vehicles_to_stop):
    return np.multiply(speed,np.logical_not(vehicles_to_stop))

def speed_up_to_match():
    pass

def slow_down_to_match():
    pass

def sim_tick(fronts, lengths, speeds, accelerations, target_speeds, loop_length):


    # needs_to_act = np.ones(len(fronts))
    # needs_to_stop = should_stop(fronts, lengths, speeds, loop_length)
    # difference_of_speeds = get_difference_of_speeds(speeds)
    # cars_that_are_too_close = are_too_close(fronts, lengths, speeds, loop_length)
    # relative_speeds_of_cars_that_are_too_close = [[difference_of_speeds[this_car][too_close] for too_close in too_close_cars] for this_car, too_close_cars in enumerate(cars_that_are_too_close)]
    # minimum_relative_speeds = []
    # for each_set_of_speeds in relative_speeds_of_cars_that_are_too_close:
    #     minimum_relative_speed = None
    #     if len(each_set_of_speeds) > 0
    #         minimum_relative_speed = min(each_set_of_speeds)
    #     minimum_relative_speeds.append(minimum_relative_speed)


def main():
    positions = np.linspace(0,999,num = 30, endpoint = False)
    speeds = np.zeros(30)

    # if will thenstop
    # else if random breaking break
    #else if too close
        #if rear is faster match speeds
        #if rears is slower accelerate
    #else if too slow speed up





if __name__ == '__main__':
    main()
