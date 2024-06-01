import unittest

from lib.solutions.HLO.hello_solution import hello


class HelloTest(unittest.TestCase):

    def test_hello(self):
        for friend_name in (
            'Jeremy',
            'Kyle',
            None,
            1
        ):
            with self.subTest(f'{friend_name=}'):
                result = hello(friend_name)
                if friend_name is None:
                    self.assertEqual(result, 'hello')
                else:
                    self.assertIn(str(friend_name), result)


if __name__ == '__main__':
    unittest.main()

