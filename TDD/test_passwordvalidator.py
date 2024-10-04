import unittest
import password_validator

class TestPasswordvalidator(unittest.TestCase):
    def test_passwordsecure(self):  # does it have all the requirements needed
        password = "Pass123@me?"
        secure = password_validator.is_password_secure(password)  # passing the password and calling the function in file
        self.assertTrue(secure)  # test will pass if the password is secure

    def test_passwordshort(self):  # will return False because of the length False = False so it will pass
        password = "Pass12"
        short = password_validator.is_password_secure(password)
        self.assertFalse(short)

    def test_password_no_upper_or_lower(self):  # will return False because of no letters
        password = "1234567@8"
        noletters = password_validator.is_password_secure(password)
        self.assertFalse(noletters)

    def test_password_no_special(self):  # returns False because of no special characters requirement met
        password = "Pass12345"
        no_special = password_validator.is_password_secure(password)
        self.assertFalse(no_special)

    def test_password_no_digits(self):  # returns False because no digits present
        password = "1234567@8"
        nodigits = password_validator.is_password_secure(password)
        self.assertFalse(nodigits)

    def test_password_no_upper(self):  # returns False no upper letters present.
        password = "pass@1234"
        noupper = password_validator.is_password_secure(password)
        self.assertFalse(noupper)


if __name__ == "__main__":
    unittest.main()