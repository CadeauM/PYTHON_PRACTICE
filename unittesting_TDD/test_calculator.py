import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add_functionality(self):
        result = calculator.calc_add(10, 20)
        self.assertEqual(result, 30)

    def test_add_functionality_negativenum(self):
        num1 = -10
        num2 = -20
        self.assertEqual(calculator.calc_add(num1, num2), -30)


if __name__ == "__main__":
    unittest.main()
