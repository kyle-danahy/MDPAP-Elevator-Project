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

        
if __name__ == '__main__':
    unittest.main()