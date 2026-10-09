import unittest
from demo import calculate_discount


class TestDiscount(unittest.TestCase):
    def test_calculate_discount(self):
        # 1000 par 10% discount = 900
        self.assertEqual(calculate_discount(1000.0, 10.0), 900.0)

    def test_zero_discount(self):
        # 500 par 0% discount = 500
        self.assertEqual(calculate_discount(500.0, 0.0), 500.0)


if __name__ == "__main__":
    unittest.main()
