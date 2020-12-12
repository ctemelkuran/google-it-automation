import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Abaci, Fatma"
        expected = "Fatma Abaci"
        self.assertEqual(rearrange_name(testcase), expected) #assertEqual: both arguments are equal

unittest.main()
