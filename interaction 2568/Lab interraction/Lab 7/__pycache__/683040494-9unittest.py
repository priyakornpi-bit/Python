# Name: Priyakorn Pichitmarn
# Student 6830040494-9

# Imports
import unittest
from area import calculate_area


# Test cases for calculate_area
class TestAreaCalculation(unittest.TestCase):
    # Normal numeric inputs
    def test_positive_numbers(self):
        self.assertEqual(calculate_area(4, 5), 20)
        self.assertEqual(calculate_area(2, 3), 6)

    def test_zero(self):
        self.assertEqual(calculate_area(0, 5), 0)
        self.assertEqual(calculate_area(7, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(calculate_area(-4, 5), -20)
        self.assertEqual(calculate_area(-2, -3), 6)

    # Invalid input types should raise TypeError
    def test_invalid_type_string(self):
        self.assertRaises(TypeError, calculate_area, "four", 5)
        self.assertRaises(TypeError, calculate_area, 4, "five")

        # Example using context manager style
        with self.assertRaises(TypeError):
            calculate_area("four", 5)

    def test_invalid_type_none(self):
        self.assertRaises(TypeError, calculate_area, None, 5)
        self.assertRaises(TypeError, calculate_area, 4, None)

        with self.assertRaises(TypeError):
            calculate_area(None, 5)

    def test_invalid_type_list(self):
        self.assertRaises(TypeError, calculate_area, [4], 5)
        self.assertRaises(TypeError, calculate_area, 4, [5])

        with self.assertRaises(TypeError):
            calculate_area([4], 5)


# Run tests directly from this file
if __name__ == '__main__':
    unittest.main()