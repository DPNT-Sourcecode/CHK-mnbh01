import unittest

from lib.solutions.CHK.checkout_solution import checkout, _condense_skus


class CheckoutTest(unittest.TestCase):

    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        '3A': 130,
        '2B': 130,
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
            ('A', 50),
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(checkout(skus), expected)


if __name__ == '__main__':
    unittest.main()




