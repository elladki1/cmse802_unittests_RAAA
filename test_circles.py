import unittest, math
from circles import circle_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test normal case
        self.assertAlmostEqual(circle_area(1), math.pi, places=12)

    def test_values(self):
        # Test negative radius should raise an error
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_types(self):
        # Test wrong type should raise an error
        with self.assertRaises(TypeError):
            circle_area("hello")

if __name__ == "__main__":
    unittest.main()

