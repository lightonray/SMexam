"import"
import unittest
from function_isfinite import my_finitefunction


class TestDevisionResults(unittest.TestCase):
    "TEST INPUTS"
    def test_finite_number(self):
        "valid testing finite number"
        valid_input = 5
        self.assertEqual(my_finitefunction(valid_input), True)

    def test_incorrect_string_value(self):
        "invalid testing string value"
        string_input = "hello"
        with self.assertRaises(TypeError):
            (my_finitefunction(string_input))

    def test_empty_value(self):
        "invalid testing empty value"
        empty_input = None
        with self.assertRaises(TypeError):
            (my_finitefunction(empty_input))

    def test_nan_value(self):
        "valid testing NaN value"
        nan_input = float("NaN")
        self.assertEqual(my_finitefunction(nan_input), False)


if __name__ == "__main__":
    unittest.main()
