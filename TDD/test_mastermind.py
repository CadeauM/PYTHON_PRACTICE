import unittest
import mastermind

class TestMastermind(unittest.TestCase):
    def test_allcorrect_colorandpos(self):  # when they are all correct no correct-ish colors
        result = mastermind.compare_codes("RGBY", "RGBY")
        self.assertEqual(result, (4, 0))

    def test_midcorrect(self):  # when some are correct
        result = mastermind.compare_codes("RGYB", "RGBY")
        self.assertEqual(result, (2, 2))

    def test_nomatch(self):  # when there is no match
        result = mastermind.compare_codes("YYYY", "RGBY")
        self.assertEqual(result, (1, 0))

if __name__ == "__main":
    unittest.main()
    