import unittest

from lib.solutions.SUM import sum_solution


class TestSum(unittest.TestCase):
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3


if __name__ == '__main__':
    unittest.main()
