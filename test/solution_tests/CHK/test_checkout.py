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
            ('-', -1),  # invalid only
            ('A-', -1),  # mix valid + invalid
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
            ('A'*5, 200),
            ('A'*6, 250),
            ('A'*7, 300),
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

    def test_checkout_with_freebies(self):
        for skus, expected in (
            ('EE', 80),  # 2E 0B -> No freebie
            ('EB', 70),  # 1E 1B -> No freebie
            ('EEB', 80),  # 2E 1B -> 1 freebie
            ('EEBB', 110),  # 2E 2B -> 1 freebie
            ('EEEEBB', 160),  # 4E 2B -> 2 freebies
            ('EEEEEBB', 200),  # 5E 2B -> 2 freebies

            ('F'*1, 10),
            ('F'*2, 20),
            ('F'*3, 20),
            ('F'*4, 30),
            ('F'*5, 40),
            ('F'*6, 40),
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(checkout(skus), expected)

    def test_new_policies_r04(self):
        # These should probably go in the other tests but I'm flagging a bit and don't want to
        # lose track of which ones are tested / untested
        # I want to avoid a penalty, so I'm gonna code up all the new singles as well...
        for skus, expected in (
            ('G', 20),
            ('H', 10),
            ('I', 35),
            ('J', 60),
            ('K', 70),
            ('L', 90),
            ('M', 15),
            ('N', 40),
            ('O', 10),
            ('P', 50),
            ('Q', 30),
            ('R', 50),
            ('S', 20),
            ('T', 20),
            ('U', 40),
            ('V', 50),
            ('W', 20),
            ('X', 17),
            ('Y', 20),
            ('Z', 21),

            ('H'*5, 45),
            ('H'*10, 80),
            ('H'*15, 125),

            ('KK', 120),
            ('KKK', 190),
            ('KKKK', 240),

            ('NNN', 120),
            ('NNNM', 120),
            ('NNNMM', 135),

            ('P'*5, 200),
            ('Q'*3, 80),
            
            ('RRR', 150),
            ('RRRQ', 150),

            ('U'*3, 120),
            ('U'*4, 120),
            ('U'*5, 160),

            ('V'*2, 90),
            ('V'*3, 130),
            ('V'*4, 180),

        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(checkout(skus), expected)

    def test_group_discounts(self):
        for skus, expected in (
            ('ST', 40),
            ('STS', 45),
            ('STST', 65),
            ('STSTS', 85),
            ('STSTST', 90),
            ('STX', 45),
            ('XYZ', 45),
            ('XZZX', 45 + 17),  # most expensive ones should be free (to favor the customer)
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(checkout(skus), expected)

if __name__ == '__main__':
    unittest.main()





