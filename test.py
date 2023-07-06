# Unit tests for rest api functions in main.py
import unittest 
import main

class TestMain(unittest.TestCase):
    def test_get(self):
        self.assertEqual(main.home_page(), 'welcome to the home page!')

    def test_get_sensors(self):
        #Test that we get the json response
        # Really lazy test, check the response looks like JSON.
        self.assertEqual(main.get_sensors().startswith('['), True)
        self.assertEqual(main.get_sensors().endswith(']'), True)

    def test_average_temperature(self):
        #Test that we get the a json response
        # Really lazy test, check the response looks like JSON.
        self.assertEqual(main.get_sensor_temperature(1).startswith('['), True)
        self.assertEqual(main.get_sensor_temperature(1).endswith(']'), True)
    
    


if __name__ == '__main__':
    unittest.main()


