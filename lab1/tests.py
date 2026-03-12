from calculator import *
import unittest

class TestCase(unittest.TestCase):
    def test_is_empty(self):
        v = Add("")
        self.assertEqual(v,0)

    def test_one_parameter(self):
        v=Add("1")
        self.assertEqual(v,1)

    def test_two_parameters(self):
        v=Add("1,2")
        self.assertEqual(v,3)

    def test_more_than_one_digit(self):
        v=Add("11,22")
        self.assertEqual(v,33)

    def test_more_than_two_parameters(self):
        v=Add("1,2,3,4")
        self.assertEqual(v,10)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Add("a,b,c")

    def test_new_line_character(self):
        v=Add("1\n2,3")
        self.assertEqual(v,6)

    def test_new_line_and_comma(self):
        with self.assertRaises(ValueError):
            Add("1,\n")