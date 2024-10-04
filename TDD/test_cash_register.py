import unittest
import cash_register

class TestCashregister(unittest.TestCase):
    def test_nochange(self):
        result = cash_register.change(1000,1000)
        self.assertEqual(result, {})

    def test_nocoins(self):
        result = cash_register.change(1800, 2000)
        self.assertEqual(result, {'R2': 1})

    def test_largeramount(self):
        result = cash_register.change(13000, 15000)
        self.assertEqual(result, {'R20': 1})

if __name__ == "__main__":
    unittest.main()