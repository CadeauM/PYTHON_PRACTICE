import unittest
import number_representations

class TestNumberrepresentation(unittest.TestCase):
    def test_simplenumbers(self):  # tests the simple numbers 
        result = number_representations.to_roman_numeral(1)
        self.assertEqual(result, "I")

    def test_requiresubtraction(self):  # tests numbers that require subtraction
        result = number_representations.to_roman_numeral(49)
        self.assertEqual(result, "XLIX")
    
    def test_complexnumbers(self):  # tests numbers that are complex and have a whole process
        result = number_representations.to_roman_numeral(1987)
        self.assertEqual(result, "MCMLXXXVII")

    def test_maxnumber(self):  # tests numbers that are complex and have a whole process
        result = number_representations.to_roman_numeral(1000)
        self.assertEqual(result, "M")

    def test_leastnumber(self):  # tests numbers that are complex and have a whole process
        result = number_representations.to_roman_numeral(0)
        self.assertEqual(result, "")



if __name__ == "__main__":
    unittest.main()