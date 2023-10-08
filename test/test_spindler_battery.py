import unittest
from datetime import datetime
from spindler_battery import Spindler_Battery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2022, 1, 1)
        battery = Spindler_Battery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime(2021, 1, 1)
        current_date = datetime(2022, 1, 1)
        battery = Spindler_Battery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
