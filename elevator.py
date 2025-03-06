# ASSUMPTIONS: all floors are non-negative
#               all floors are integers
from argparse import ArgumentParser

# constant for time to travel a single floor
SINGLE_FLOOR_TRAVEL_TIME = 10

def calculate_travel_time(floors_to_visit):
    total_travel_time = 0
    # start range at 1 since we don't need to calculate travel time for starting floor
    for index in range(1, len(floors_to_visit)):
        total_travel_time = total_travel_time + (abs(floors_to_visit[index] - floors_to_visit[index - 1]) 
                                                        * SINGLE_FLOOR_TRAVEL_TIME)
        index = index + 1
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