import unittest
from distance import distance

class DistanceTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(distance(0,0,0,0),0)
    def test_x_diff(self):
        self.assertEqual(distance(0,0,10,0),10)
    def test_y_diff(self):
        self.assertEqual(distance(0,0,0,10),10)
    def test_x_y_diff(self):
        self.assertEqual(distance(1,8,10,10),7)
    def test_x_y_fail(self):
        self.assertEqual(distance(1, 8, 10, 10), 5)
    def test_x_y_err_call(self):
        self.assertEqual(distance(1, 10, 10), 5)