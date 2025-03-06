# MDPAP-Elevator-Project
Code that simulates an elevator

Provided a list of floors to visit (first number in the list is assumed to be the starting floor), this
function will calculate the amount of time it will take to travel to all floors in the list, with a constant
of 10 seconds of travel time per floor. The function will return a dictionary with the 'total_travel_time'
in seconds, as well as the list of floors visited including the starting floor.

to run the script, execute `python3 elevator.py --floors 1 2 3 4`, where anything after the --floors flag should
be an integer number and each floor number should be separated by a space.