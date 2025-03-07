# ASSUMPTIONS: all floors are integers, should be greater than 0 but I added a check just in case
from argparse import ArgumentParser

# constant for time to travel a single floor
SINGLE_FLOOR_TRAVEL_TIME = 10

def calculate_travel_time(floors_to_visit):
    # assuming the first floor of a building should be 1, should not allow a floor number of 0
    if 0 in floors_to_visit:
        return "0 is not a valid floor number, please choose positive values only"

    total_travel_time = 0
    # start at index 1 since we don't need to calculate travel time for starting floor
    for index in range(1, len(floors_to_visit)):
        # check that each value is a positive number
        if str(floors_to_visit[index]).isnumeric():
            total_travel_time = total_travel_time + (abs(floors_to_visit[index] - floors_to_visit[index - 1]) 
                                                        * SINGLE_FLOOR_TRAVEL_TIME)
            index = index + 1
        else:
            return f"'{floors_to_visit[index]}' is not a valid floor number. Please make sure it is a positive integer."
    return {'total_travel_time': total_travel_time, 'floors_visited': floors_to_visit}

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--floors",
                        nargs='+',
                        type=int,
                        help="please provide the floors you would like to visit. each floor should be separated by a space",
                        required=True)

    travel_info = calculate_travel_time(parser.parse_args().floors)
    print(travel_info)