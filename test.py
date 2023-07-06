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
    
    def test_get_sensor(self):
        #Test that we get the json response
        # Really lazy test, check the response looks like JSON.
        self.assertEqual(main.get_sensor(1).startswith('['), True)
        self.assertEqual(main.get_sensor(1).endswith(']'), True)

    def test_get_sensor_temperature(self):
        #Test that we get the a json response
        # Really lazy test, check the response looks like JSON.
        self.assertEqual(main.get_sensor_temperature(1).startswith('['), True)
        self.assertEqual(main.get_sensor_temperature(1).endswith(']'), True)
        self.assertEqual(main.get_sensor_temperature(1).startswith('[[6'), True)   
    
    def test_get_sensor_humidity(self):
        #Test that we get the a json response
        # Really lazy test, check the response looks like JSON.
        self.assertEqual(main.get_sensor_humidity(1).startswith('['), True)
        self.assertEqual(main.get_sensor_humidity(1).endswith(']'), True)
        self.assertEqual(main.get_sensor_humidity(1).startswith('[[51'), True)
    
    def test_get_sensor_data(self):
        #Test that we get the a json response
        # Really lazy test, check the response looks like JSON.
        self.assertEqual(main.get_sensor_data(1, '12-07-2023').startswith('['), True)
        self.assertEqual(main.get_sensor_data(1, '12-07-2023').endswith(']'), True)
        self.assertEqual(main.get_sensor_data(1, '12-07-2023').startswith('[[2, 1'), True)

    def test_get_sensor_humidity_date(self):
        #Test that we get the a json response
        # Really lazy test, check the response looks like JSON.
        # Also test that the result looks correct
        self.assertEqual(main.get_sensor_humidity_date(1, '12-07-2023').startswith('['), True)
        self.assertEqual(main.get_sensor_humidity_date(1, '12-07-2023').endswith(']'), True)
        self.assertEqual(main.get_sensor_humidity_date(1, '12-07-2023').startswith('[[48'), True)

    def test_get_sensor_temperature_date(self):
        #Test that we get the a json response
        # Really lazy test, check the response looks like JSON.
        # Also test that the result looks correct
        self.assertEqual(main.get_sensor_temperature_date(1, '2023-07-01').startswith('['), True)
        self.assertEqual(main.get_sensor_temperature_date(1, '2023-07-01').endswith(']'), True)
        self.assertEqual(main.get_sensor_temperature_date(1, '12-07-2023').startswith('[[-4'), True)

    


if __name__ == '__main__':
    unittest.main()


