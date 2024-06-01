import unittest

from lib.solutions.CHK.checkout_solution import (
    PRICES,
    _condense_skus,
    checkout, 
)


class CheckoutTest(unittest.TestCase):

    def test_condense(self):
        for skus, expected in (
            (None, {}),       # falsey
            ('', {}),         # falsey
            ('ABC',    {'A': 1, 'B': 1, 'C': 1}),
            ('ABBC',   {'A': 1, 'B': 2, 'C': 1}),
            ('ABBCCC', {'A': 1, 'B': 2, 'C': 3}),
        ):
            with self.subTest(f'{skus=}'):
                self.assertDictEqual(_condense_skus(skus), expected)

    def test_checkout_singles(self):
        for skus, expected in (
            (None, 0),
            ('', 0),
            ('A', 50),
            ('B', 30),
            ('C', 20),
            ('D', 15),
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(checkout(skus), expected)

    def test_checkout_invalid(self):
        for skus, expected in (
            ('E', -1),  # invalid only
            ('AE', -1),  # mix valid + invalid
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(checkout(skus), expected)

    def test_checkout_multibuys_single_product(self):
        for skus, expected in (
            (None, 0),
            ('', 0),
            ('A'*1, 50),
            ('A'*2, 100),
            ('A'*3, 130),
            ('A'*4, 180),
            ('A'*5, 230),
            ('A'*6, 260),
            ('A'*7, 310),
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(checkout(skus), expected)

    def test_checkout_multibuys_multiple_products(self):
        for skus, expected in (
            ('AB', 80),
            ('ABD', 95),
            ('BBD', 60),
            ('AAABB', 175),
            ('ADBACBA', 210),
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(checkout(skus), expected)

if __name__ == '__main__':
    unittest.main()



