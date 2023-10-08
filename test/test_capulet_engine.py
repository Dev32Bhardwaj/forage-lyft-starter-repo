import unittest

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced_true(self):
        engine = CapuletEngine(current_mileage=35000, last_service_mileage=20000)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_be_serviced_false(self):
        engine = CapuletEngine(current_mileage=25000, last_service_mileage=30000)
        self.assertFalse(engine.engine_should_be_serviced())

    def test_engine_should_be_serviced_edge_case(self):
        engine = CapuletEngine(current_mileage=60000, last_service_mileage=30000)
        self.assertTrue(engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
