# traffic-simulation

##What we want our program to do
We have a 1 kilometer section of road being built and do not know what the speed limit needs to be. Simulate 1 kilometer of road. Even though this road is not circular, treat it as such in order to generate a continuous flow of traffic.
When you start the simulation, it adds 30 cars to the road per kilometer, evenly spaced. Then run the simulation for one minute to get a continuous, randomized stream of traffic.

##What our program does
Our program generates a number of cars, tracks their speed, location and proximity to other cars. Every second it evaluates probability of collision to determine if the car should slow down, speed up or stop.

##Jupyter Notebook
The notebook for this program runs the simulation 100 times for 60 seconds. We plotted the locations, speeds, mean, and standard deviation for the last simulation in the group. We made our speed limit recommendation on the median of the recommendations we would have made for each loop of the simulation. We discard the transient to achieve steady state.
