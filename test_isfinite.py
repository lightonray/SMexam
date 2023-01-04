import unittest
from function_isfinite import my_finitefunction


class TestDevisionResults(unittest.TestCase):
    def test_finite_number(self):
        self.assertEqual(my_finitefunction(5), True)
        
    def test_incorrect_value(self):
        with self.assertRaises(TypeError):
            self.assertEqual(my_finitefunction("hello"), True)

    def test_empty_value(self):
        with self.assertRaises(TypeError):
            self.assertEqual(my_finitefunction(None), True)

        
    
if __name__ == '__main__':
    unittest.main()