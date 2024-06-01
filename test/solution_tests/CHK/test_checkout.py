import unittest

from lib.solutions.CHK.checkout_solution import checkout, _condense_skus


class CheckoutTest(unittest.TestCase):

    prices = {
        'A': {1: 50, 3: 130},
        'B': {1: 30, 2: 45},
        'C': {1: 20},
        'D': {1: 15},
    }

    def test_condense(self):
        for skus, expected in (
            (None, ''),             # falsey
            ('', ''),               # falsey
            ('C', '1C'),            # single still gets formatted
            ('ABC', '1A1B1C'),      # multiple singles
            ('ABBC', '1A2B1C'),     # multiples, single at start
            ('AAABBC', '3A2B1C'),   # multiples, single at end
            ('AAABCC', '3A1B2C'),   # multiples, single in middle
            ('AAABBCC', '3A2B2C'),  # multiples throughout
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(_condense_skus(skus), expected)

    def test_checkout_singles(self):
        for skus, expected in (
            (None, 0),
            ('', 0),
            ('A', 50),
            ('B', 30),
            ('C', 20),
            ('D', 50),
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(checkout(skus), expected)

    def test_checkout_multibuys(self):
        # I have jsut realised that if I buy 5A, I need to apply the discount on only the first 3...
        # *sigh*...
        for skus, expected in (
            (None, 0),
            ('', 0),
            ('A', 50),
            ('B', 30),
            ('C', 20),
            ('D', 50),
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(checkout(skus), expected)

if __name__ == '__main__':
    unittest.main()





