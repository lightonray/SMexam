import unittest
from function_isfinite import my_finitefunction



class TestDevisionResults(unittest.TestCase):
    def test_finite_number(self):
        valid_input = 5;
        self.assertEqual(my_finitefunction(valid_input), True)
        
    def test_incorrect_string_value(self):
        string_input = "hello"
        with self.assertRaises(TypeError):
            self.assert_(my_finitefunction(string_input))

    def test_empty_value(self):
        empty_input = None
        with self.assertRaises(TypeError):
            self.assert_(my_finitefunction(empty_input))
            
    def test_NaN_value(self):
        NaN_input = float('NaN')
        self.assertEqual(my_finitefunction(NaN_input), False)

        
    
if __name__ == '__main__':
    unittest.main()