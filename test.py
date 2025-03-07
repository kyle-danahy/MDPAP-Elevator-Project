import unittest
import elevator

class TestCalculateTravelTime(unittest.TestCase):
    def test_provided_example(self):
        self.assertEqual(elevator.calculate_travel_time([12, 2, 9, 1, 32]), 
                            {'total_travel_time': 560, 'floors_visited': [12, 2, 9, 1, 32]})
        
    def test_two_floors(self):
        self.assertEqual(elevator.calculate_travel_time([1, 10]),
                         {'total_travel_time': 90, 'floors_visited': [1, 10]})
        
    def test_repeated_floors(self):
        self.assertEqual(elevator.calculate_travel_time([1, 5, 7, 5, 3, 5]),
                         {'total_travel_time': 120, 'floors_visited': [1, 5, 7, 5, 3, 5]})
        
    def test_going_to_current_floor(self):
        self.assertEqual(elevator.calculate_travel_time([3, 5, 6, 6]),
                         {'total_travel_time': 30, 'floors_visited': [3, 5, 6, 6]})
        
    # per wikipedia, the tallest building in the world currently is 163 floors
    def test_maximum_floors(self):
        self.assertEqual(elevator.calculate_travel_time([1, 57, 109, 163, 25, 133]),
                         {'total_travel_time': 4080, 'floors_visited': [1, 57, 109, 163, 25, 133]})

    def test_zero_first(self):
        self.assertEqual(elevator.calculate_travel_time([0, 10]),
                         "0 is not a valid floor number, please choose positive values only")
        
    def test_zero_in_list(self):
        self.assertEqual(elevator.calculate_travel_time([3, 17, 5, 0, 12]),
                         "0 is not a valid floor number, please choose positive values only")
        
    def test_non_numeric(self):
        self.assertEqual(elevator.calculate_travel_time([1, 'a', 3, 10]),
                         "'a' is not a valid floor number. Please make sure it is a positive integer.")
        
    def test_negative_floor_number(self):
        self.assertEqual(elevator.calculate_travel_time([10, 7, 33, -4, 15]),
                         "'-4' is not a valid floor number. Please make sure it is a positive integer.")

if __name__ == '__main__':
    unittest.main()