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
            ('ABC','1A1B1C'),
            ('AAABBC','3A2B1C'),
        ):
            with self.subTest(f'{skus=}'):
                self.assertEqual(_condense_skus(skus), expected)


    def test_checkout_singles(self):
        pass


if __name__ == '__main__':
    unittest.main()

