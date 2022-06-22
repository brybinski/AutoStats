import unittest
import DataToProcess
from Variable import Variable

# TODO: Tests of this thing...
class TestStatsCount(unittest.TestCase):
    x = Variable([10., 2., 3., 4, 5], 0)

    def test_mean(self):
        self.assertTrue(self.x.mean == 4.8)

    def test_max(self):
        self.assertTrue(self.x.max == 10.)

    def test_min(self):
        self.assertTrue(self.x.min == 2.)

    def test_median(self):
        self.assertTrue(self.x.median == 4)


class TestDataProperties(unittest.TestCase):
    def test_data(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
