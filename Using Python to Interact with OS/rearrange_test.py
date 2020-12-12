import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Abaci, Fatma"
        expected = "Fatma Abaci"
        self.assertEqual(rearrange_name(testcase), expected) #assertEqual: both arguments are equal

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)

    def test_double_name(self):
        testcase = "Tolkein, John R. R."
        expected = "John R. R. Tolkein"
        self.assertEqual(rearrange_name(testcase),expected)

    def test_one_name(self):
        testcase = "Çığır"
        expected = "Çığır"
        self.assertEqual(rearrange_name(testcase),expected)

unittest.main()
