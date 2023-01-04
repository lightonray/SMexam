import unittest
from function_isfinite import my_finitefunction


class TestDevisionResults(unittest.TestCase):
    def test_finite_number(self):
        self.assertEqual(my_finitefunction(5), True)


if __name__ == '__main__':
    unittest.main()