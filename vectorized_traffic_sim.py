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
