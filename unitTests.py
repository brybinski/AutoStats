import unittest
import DataMatrix
from Variable import Variable

# TODO: Tests of this thing...
class TestStatsCount(unittest.TestCase):
    x = Variable([1.00,
                  5.00,
                  8.00,
                  7.00,
                  5.00,
                  56.00,
                  6.00,
                  8.00,
                  4.00,
                  1.00], 1)

    print(x)

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
