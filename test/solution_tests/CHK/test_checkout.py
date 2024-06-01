import unittest

from lib.solutions.CHK.checkout_solution import checkout


class CheckoutTest(unittest.TestCase):

    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        '3A': 130,
        '2B': 130,
    }

    def test_checkout_singles(self):
        pass


if __name__ == '__main__':
    unittest.main()
