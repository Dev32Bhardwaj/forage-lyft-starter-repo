import unittest

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced_true(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_be_serviced_false(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
