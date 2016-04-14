# traffic-simulation

## What we want the program to do

create car objects that belong to a road object that make an estimate of the next position every second(or so).

treat road as a circle, going one way, one lane

##describe cars
-target and current speeds
-length
-acceleration rates and breaking chance
-behavior

who keeps track of where the cars are? the road or the cars individually?
-the car keeps track of its own location and asks the road where the other cars are
