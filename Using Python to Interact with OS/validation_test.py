import unittest
from validation import validate_user

class TestValidate(unittest.TestCase):
    def test_something(self):
        self.assertEqual(validate_user("valid",3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_chars(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)

if __name__ == '__main__':
    unittest.main()
