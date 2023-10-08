import unittest

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced_true(self):
        engine = WilloughbyEngine(current_mileage=70000, last_service_mileage=10000)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_be_serviced_false(self):
        engine = WilloughbyEngine(current_mileage=50000, last_service_mileage=10000)
        self.assertFalse(engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
