import unittest
from datetime import datetime
from your_module import Nubbin_Battery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2023, 1, 1)
        battery = Nubbin_Battery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        last_service_date = datetime(2022, 1, 1)
        current_date = datetime(2023, 1, 1)
        battery = Nubbin_Battery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()