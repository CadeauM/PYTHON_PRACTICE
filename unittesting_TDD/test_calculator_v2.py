import unittest
import calculator_v2

class TestCalculatorv2(unittest.TestCase):
    def test_add_functionality(self):
        calc1 = calculator_v2(10, 30)  # creates an instance
        result = calc1.calc_add()
        self.assertEqual(result, 40)


if __name__ == "__main__":
    unittest.main()