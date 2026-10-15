import unittest


def check_password(password):
    if len(password) < 8:
        raise ValueError("Password is too short")
    return True

class TestCheckPasswordLength(unittest.TestCase):
    def test_short_password(self):
        with self.assertRaises(ValueError):
            check_password(password="234")
    def test_long_password(self):
        self.assertTrue(check_password(password="ase123"))
